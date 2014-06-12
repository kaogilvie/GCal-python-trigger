import creds
import requests
import json
import datetime
from requests.auth import AuthBase

#attributes received from python script (extensible)
text_to_append_to_event = 'Foo'
text_for_new_event = 'Foo2'
date_of_event = datetime.date(2014,06,10)
invitee = 'foo@fookid.com'
time_of_event_start = 'T08:00:00.000-05:00:00'
time_of_event_end = 'T08:30:00.000-05:00:00'

#set up parameters
working_calendar_id = creds.working_calendar_id
startDate = str(date_of_event)+time_of_event_start
endDate = str(date_of_event)+time_of_event_end

#fetch event from designated time if it exists
query_params = {	'timeMin'	:startDate,
					'timeMax'	:endDate	}

#set up create event data
create_event_data = {
						'start'	:	{'dateTime':	startDate},
						'summary'	:	text_for_new_event,
						'anyoneCanAddSelf' : True,
						'attendees':	[
											{'email'	: invitee}
										],
						'end'		:	{'dateTime': 	endDate}
					}

def fetch_access_token():
	#use refresh token from trig_init to fetch access token
	payload = { 	'refresh_token' : creds.refresh_token,
						'client_id'		: creds.client_id,
						'client_secret'	: creds.client_secret,
						'grant_type'	: 'refresh_token'
					}
	r = requests.post('https://accounts.google.com/o/oauth2/token', data=payload)

	#set up authentication headers
	json_resp = json.loads(r.content)
	access_token = json_resp['access_token']
	custom_headers = {	'Authorization': 'Bearer '+access_token,
						'Content-type' : 'application/json'}

	return custom_headers

def trigger_event(working_calendar_id, custom_headers, query_params, create_event_data, text_to_append_to_event):

	events_url = 'https://www.googleapis.com/calendar/v3/calendars/'+working_calendar_id+'/events'
	calendar = requests.get(events_url, headers=custom_headers, params=query_params)
	response = json.loads(calendar.content)

	if len(response['items']) < 1:
		create_event_url = 'https://www.googleapis.com/calendar/v3/calendars/'+working_calendar_id+'/events'
		r = requests.post(url=create_event_url, headers=custom_headers, data=json.dumps(create_event_data))
		r_dict = json.loads(r.content)
		print "Created new event; named: "+r_dict['summary']+"."

	else:

		#if an event exists at the correct time, update it
		for event in response['items']:

			#update the summary variable
			title_of_event = event['summary']
			add_text = ', '+text_to_append_to_event
			title_of_event = title_of_event+text_to_append_to_event
			event['summary'] = title_of_event

			#necessary for patch request
			event_id = event['id']
			event_dict = {'summary': title_of_event}
			patch_url = 'https://www.googleapis.com/calendar/v3/calendars/'+working_calendar_id+'/events/'+event_id

			#update patch request
			url = requests.patch(patch_url, headers=custom_headers, data=json.dumps(event_dict))
			url_dict = json.loads(url.content)
			print "Updated event to "+url_dict['summary']+'.'
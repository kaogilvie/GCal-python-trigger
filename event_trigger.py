import creds
import requests
import json
import datetime
from requests.auth import AuthBase

post_payload = { 	'refresh_token' : creds.refresh_token,
					'client_id'		: creds.client_id,
					'client_secret'	: creds.client_secret,
					'grant_type'	: 'refresh_token'
				}

r = requests.post('https://accounts.google.com/o/oauth2/token', data=payload)

#set up authentication headers
json_resp = json.loads(r.content)
access_token = json_resp['access_token']
custom_headers = {'Authorization': 'Bearer '+access_token}

#set up parameters
search_query = 'Winners'
working_calendar_id = creds.working_calendar_id
startDate = str(datetime.date(2014,06,10))+'T00:00:00-05:00:00'
endDate = str(datetime.date(2014,06,10))+'T15:00:00-05:00:00'
break_variable = False

#attributes received from python script
winner = 'foo'
date_of_winner = datetime.date(2014,06,10)

#now the actual calendar API actions...
query_params = {	'timeMin'	:startDate,
					'timeMax'	:endDate,
					'q'			:search_query }
events_url = 'https://www.googleapis.com/calendar/v3/calendars/'+working_calendar_id+'/events'

calendar = requests.get(events_url, params=query_payload)
response = json.loads(calendar.content)

#if an event exists at the correct time, update it
for event in response['items']:

	#update the summary variable
	title_of_event = event['summary']
	add_winner_text = ', '+winner
	title_of_event = title_of_event+add_winner_text
	event['summary'] = title_of_event

	#get event id
	event_id = event['id']

	event_dict = {'summary': title_of_event}
	event_json = json.dumps(event)

	patch_url = 'https://www.googleapis.com/calendar/v3/calendars/'+working_calendar_id+'/events/'+event_id

	url = requests.patch(patch_url, headers=custom_headers, data=event_json)
	print url.content

	break_variable = True

if break_variable == False:
	pass

#if an event doesn't exist, create it
#invite whoever is running the script to the event so they get notifications when it changes

#else:
#	print "Updated winner event for "+str(date_of_winner)+" to include "+winner+'.'
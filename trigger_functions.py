import credentials as creds
import requests
import json
import datetime
from requests.auth import AuthBase

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

def get_events_calendar(working_calendar_id, custom_headers, query_params):
	#get the events calendar response from Google
	events_url = 'https://www.googleapis.com/calendar/v3/calendars/'+working_calendar_id+'/events'
	calendar = requests.get(events_url, headers=custom_headers, params=query_params)
	response = json.loads(calendar.content)
	return response

def create_event(custom_headers, create_event_data):
	#creates a new event
	create_event_url = 'https://www.googleapis.com/calendar/v3/calendars/'+working_calendar_id+'/events'
	r = requests.post(url=create_event_url, headers=custom_headers, data=json.dumps(create_event_data))
	r_dict = json.loads(r.content)
	print "Created new event; named: "+r_dict['summary']+"."

def update_event(response, custom_headers, working_calendar_id):
	#updates an existing event
	event_id = response['items'][0]['id']
	patch_url = 'https://www.googleapis.com/calendar/v3/calendars/'+working_calendar_id+'/events/'+event_id

	url = requests.patch(patch_url, headers=custom_headers, data=json.dumps(update_event_dict))
	url_dict = json.loads(url.content)
	print "Updated event to "+url_dict['summary']+'.'

def update_events(response, update_event_dict, working_calendar_id):
	#updates all events in the response object from get_events_calendar
	for event in response['items':]

		event_id = event['id']
		patch_url = 'https://www.googleapis.com/calendar/v3/calendars/'+working_calendar_id+'/events/'+event_id

		url = requests.patch(patch_url, headers=custom_headers, data=json.dumps(update_event_dict))
		url_dict = json.loads(url.content)
		print "Updated event to "+url_dict['summary']+'.'
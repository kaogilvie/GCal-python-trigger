import creds
import requests
import json

payload = { 'refresh_token' : creds.refresh_token,
			'client_id'		: creds.client_id,
			'client_secret'	: creds.client_secret,
			'grant_type'	: 'refresh_token'
			}

r = requests.post('https://accounts.google.com/o/oauth2/token', data=payload)

json_resp = json.loads(r.content)
access_token = json_resp['access_token']
custom_headers = {'Authorization: Bearer': access_token}

#authenticate with scope
scope = 'https://www.googleapis.com/auth/calendar'

#python script fires something off
#now the actual calendar API actions...

working_calendar_id = 'kyle@wellandlighthouse.com'

payload = {'access_token':access_token}
calendar = requests.get('https://www.googleapis.com/calendar/v3/calendars/'+working_calendar_id, data=payload)

print calendar.url
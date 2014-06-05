import requests
import creds
import json

payload = { 'response_type' : 'code',
			'redirect_uri' : 'urn:ietf:wg:oauth:2.0:oob',
			'client_id'	: creds.client_id,
#			'client_secret' : creds.client_secret,
			'scope'		: 'https://www.googleapis.com/auth/calendar'
			}

r = requests.post('https://accounts.google.com/o/oauth2/auth', data=payload)

print "Copy url into browser and follow authentication flow."
print r.url

authorization_code = raw_input('Enter authorization code:')

payload2 = {	'code':	authorization_code,
				'client_id' : creds.client_id,
				'client_secret': creds.client_secret,
				'redirect_uri': 'urn:ietf:wg:oauth:2.0:oob',
				'grant_type' : 'authorization_code'}

r2 = requests.post('https://accounts.google.com/o/oauth2/token', data=payload2)

json_resp = json.loads(r2.content)
access_token = json_resp['access_token']
token_type = json_resp['token_type']
refresh_token = json_resp['refresh_token']
print access_token
print token_type
print "refresh_token: ",refresh_token
print "Add refresh_token to creds."
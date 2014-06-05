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

print access_token
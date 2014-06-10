Google Calendar API program that will trigger the creation of an event (or add to an existing event, if it exists) on the registered users calendar. Designed to bind to the end of a python script.

Uses the requests library on purpose to by-pass the confusing OAuth2 library and even more confusing errors raised when following the OAuth2 library documentation from Google. Simpler is more pythonic and other platitudes.

USAGE
=====

Must create "creds.py" -- a non-git file that contains your credentials for this project from the developers console [here](http://console.developers.google.com).*

*Meaning yes, you must register this project with the developers console.

Creds.py should contain the following:
* client_id
* cient_secret
* redirect_uri
* refresh_token

Must run "trig_init.py" first to obtain access.
* Copy printed URL into browser
* Follow authentication flow in browser
* Copy authorization code and paste into terminal
* Copy refresh token at end of script
* Paste into "creds.py" (a non-git file)

CHANGELOG
=========

5/30/2014 -- 17:00
------------------
Initial commit

6/5/2014 -- 11:00
-----------------
Authentication flow for Google Calendar API for desktop applications added up to "request_token".

6/10/2014 -- 11:30
------------------
Barebones API call in place to grab events that match a variable word from a variable time period

6/10/2014 -- 15:50
------------------
Update event fucntionality problematic--PATCH request is still erroring.
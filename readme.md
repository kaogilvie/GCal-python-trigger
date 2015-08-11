#GEvent Trigger

Google Calendar API program that will trigger the creation of an event (or add to an existing event, if it exists) on the registered users calendar. Designed to bind to the end of a python script.

Uses the requests library on purpose to by-pass the confusing OAuth2 library and even more confusing errors raised when following the OAuth2 library documentation from Google. Simpler is more pythonic and other platitudes.

##USAGE
Very functional, very class-less. Oh, the places we go...

Must create "credentials.py" -- a non-git file that contains your credentials for this project from the developers console [here](http://console.developers.google.com).*

*Meaning yes, you must register this project with the developers console.

Credentials.py should contain the following:
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

event_trigger.py & using the functions...
* Easy to nest the functions found in trigger_functions.py for exquisite workflow control
* event_triggers.py provides a few examples of workflows
* configuration.py allows for control of parameters of UPDATING, CREATING and SEARCHING for events
* Searching for events with the configuration.py SEARCH dictionary allows you to control the events you update
* CREATE dictionary in configuration.py allows control of the details of created events
* UPDATE dictionary allows control of what details get overwritten about an event on update
* All dictionaries in configuration.py are great endpoints for python script variables, allowing dynamic updating and creation of events


##CHANGELOG


###5/30/2014 -- 17:00 -- V0.1

Initial commit

###6/5/2014 -- 11:00 -- V0.2

Authentication flow for Google Calendar API for desktop applications added up to "request_token".

###6/10/2014 -- 11:30 -- V0.3

Barebones API call in place to grab events that match a variable word from a variable time period

###6/10/2014 -- 15:50 -- V0.4

Update event fucntionality problematic--PATCH request is still erroring.

###6/10/2014 -- 18:30 -- V0.5

Authentication uses Bearer Token headers instead of url query parameters.

###6/11/2014 -- 17:00 -- V0.6

POST and PATCH requests use 'Content-type: application/json' headers in order to actually update Google Calendar (IMPORTANT!!). Application works with hardcoded variables [should be passed in from python function].

###6/12/2014 -- 14:39 -- V1.0

Functional & functioned script. Parameters clear--ready for import into any python script!! (Readme updated as well).

###6/15/2015 -- 7:34 -- V1.0.1

Cleaning up repos to make presentable. Readme updated to specifically state that this is a functional script rather than an attempted package, at the moment.

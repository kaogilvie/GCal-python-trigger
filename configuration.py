"""CONFIGURATION FILE FOR EVENT_TRIGGER"""
#-----------------------------------------#
#-----------------------------------------#
#-----------------------------------------#

"""
This section mimics what can be received from any python script. These are simply examples & can all be dropped into the dictionaries below via scripting.
"""
text_to_append_to_event = 'Foo'
text_for_new_event = 'Foo2'
date_of_event = datetime.date(2014,06,10)
invitee = 'foo@fookid.com'
time_of_event_start = 'T08:00:00.000-05:00:00'
time_of_event_end = 'T08:30:00.000-05:00:00'
startDate = str(date_of_event)+time_of_event_start
endDate = str(date_of_event)+time_of_event_end


"""
necessary for all API calls
"""
working_calendar_id = 'insert relevant string id here'


"""
SEARCH RESTRICTION PARAMETERS
Examples are below. See https://developers.google.com/google-apps/calendar/v3/reference/events/list
for more search options. Add as an entry into the dictionary any restriction you wish.

NOTE ON TIMES: must be strings in the format of YYYY-MM-DDT00:00:00.000-05:00
...where the -05:00 is the relevant time zone offset if the time zone variable isn't explicitly passed into the call.
"""
query_params = {	'timeMin'	:startDate,
					'timeMax'	:endDate,
					'q'			:'example string'
						}

"""
CREATE PARAMTERS

Below is an example of this extensible dictionary. 
Simply pass in other parameters that you can find here: https://developers.google.com/google-apps/calendar/v3/reference/events/insert
and they will be added to the request body.

"""
create_event_data = {
						'start'	:	{'dateTime':	startDate},
						'summary'	:	text_for_new_event,
						'anyoneCanAddSelf' : True,
						'attendees':	[
											{'email'	: invitee},
											{'email'	: 'invitee@example.com'}
										],
						'end'		:	{'dateTime': 	endDate}
					}


"""
UPDATE PARAMETERS

This dictionary is a representation of the Google Events Resource. Anything passed into this dictionary will overwrite
the Events Resource via a PATCH HTTP request. You can find additional parameters here: https://developers.google.com/google-apps/calendar/v3/reference/events#resource
"""
update_event_data = {'summary': title_of_event}
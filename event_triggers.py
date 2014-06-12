import trigger_functions as trig
import configuration as config

"""
Some examples of how you can use these functions to create custom handlers for event updating based on certain parameters.

Can also use these skeletons in concert with the variable query_params & create_event_data dictionaries to return a very select slice of events.
"""

def trigger_unique_events(working_calendar_id, custom_headers, query_params, create_event_data, update_event_dict):
	#trigger the creation of a new event if the event doesn't already exist; if it does, trigger update to all events returned in that time period
	response = trig.get_events_calendar(working_calendar_id, custom_headers, query_params)

	if len(response['items']) < 1:
		trig.create_event(custom_headers, create_event_data)

	else:
		trig.update_events(response, custom_headers, update_event_dict, working_calendar_id)

def trigger_new_event(working_calendar_id, custom_headers, create_event_data):
	#trigger creation of new event for each call, even if event already exists at that time (this is a dumb example but you get the picture)
	trig.create_event(custom_headers, create_event_data, working_calendar_id)
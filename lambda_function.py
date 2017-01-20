import urllib2
import json
import schiene 
from schiene import schiene
import requests
import bs4


def lambda_handler(event, context):
    if (event['session']['application']['applicationId'] != [YOUR_APPLICATION_ID]):
#        raise ValueError("Invalid Application ID")
        pass
    
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']}, event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
		
		
def on_session_started(session_started_request, session):
    print "Starting new session."

def on_launch(launch_request, session):
    return get_welcome_response()

def on_intent(intent_request, session):
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "GetTrainTimes":
        return get_train_times(intent)
    elif intent_name == "KnowEnoughIntent":
        return handle_session_end_request()
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    elif intent_name == "AMAZON.CancelIntent":
        return handle_session_end_request()
    elif intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    return handle_session_end_request()
    print "Ending session."
    # Cleanup goes here...

def get_welcome_response():
    session_attributes = {}
    card_title = "SCHIENE"
    speech_output = "Welcome to where is my train. I can tell you when your next train is leaving. " \
                    "You can ask me for any connection in Germany. Where do you want to go?"
    reprompt_text = "Please ask me for the trains times from a station to another station, " \
                    "for example ask me when is the next train from Hamburg to Berlin."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Where is my train - Thanks"
    speech_output = "Thank you for using the where is my train skill.  See you next time!"
    should_end_session = True

    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))

def get_train_times(intent):
    session_attributes = {}
    card_title = "Where is my train Departures"
    speech_output = "I'm not sure which connection you wanted train times for. " \
                    "Please try again."
    reprompt_text = "I'm not sure which station you wanted train times for. " \
                    "For example, try asking when is the next train from Berlin to Stuttgart."
    
    try:
        StationOne = intent['slots']['StationOne']['value']
        StationTwo = intent['slots']['StationTwo']['value']

        s = schiene.Schiene()
        result = s.connections(StationOne,StationTwo)
        dep = result[0]['departure']
        arr = result[0]['arrival']
        price = str(result[0]['price'])
        if price != "None":
            price_txt = "The price of the ticket is "+price+" euro."
        if price == "None":
            price_txt = ""
        trans = str(result[0]['transfers'])
    

        try:
            canceled = result[0]['canceled']
        except:
            canceled = False
        try:
            delay = result[0]['delay']
        except:
            delay = None
        try: 
            ontime = result[0]['ontime']
        except:
            ontime = False
        if delay != None:
            status = "Status: delayed. "
        elif canceled == True :
            status = "Status: Important additional information for this connection. Please check the website of the German Railway to make sure this train is not cancelled. "
        elif ontime == True :
            status = "Status: on time. "
        else:
            status = ""

        dep2 = result[1]['departure']
        dep3 = result[2]['departure']
        dep4 = result[3]['departure']
        end = "Feel free to ask me for another connection."
        speech_output = "So you want to know the next train from "+StationOne+" to "+StationTwo+", the next train leaves at: "+dep+" and arrives at "+arr+". "+status+price_txt+" Number of transfers: "+trans+". Your later options to get to "+StationTwo+" are at "+dep2+", "+dep3+" and "+dep4+". "+end
    
    except:
        pass
    
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

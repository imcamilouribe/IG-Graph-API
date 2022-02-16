import re
from urllib import response
import requests
import json

def getCreds() :

    """ Get creds required for use in the applications
	
	Returns:
		dictonary: credentials needed globally
	"""

    creds = dict()
    creds['access_token'] = ''
    creds['client_id'] = ''
    creds['client_secret'] = ''
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v13.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'
    creds['page_id'] = ''
    creds['instagram_account_id'] = ''

    return creds


def makeApiCall( url, endpointParams, debug = 'no' ):

    """ Request data from endpoint with params
	
	Args:
		url: string of the url endpoint to make request from
		endpointParams: dictionary keyed by the names of the url parameters
	Returns:
		object: data from the endpoint
	"""

    data = requests.get( url, endpointParams, verify=False )

    response = dict() # hold response info
    response['url'] = url # url we are hitting
    response['endpoint_params'] = endpointParams #parameters for the endpoint
    response['endpoint_params_pretty'] = json.dumps( endpointParams, indent=4 ) # pretty print for cli
    response['json_data'] = json.loads( data.content ) # response data from the api
    response['json_data_pretty'] = json.dumps( response['json_data'], indent=4 ) # pretty print for cli

    if ( 'yes' == debug ): # display out response info
        displayApiCallData( response )

    return response # get and return content


def displayApiCallData ( response ):
    """ Print out to cli response from api call """
    
    print ( "URL:" ) # title
    print ( response['url'] ) # display url hit
    print ( "\nEndpoint Params: " ) # title
    print ( response['endpoint_params_pretty'] ) # display params passed to the endpoint
    print ( "\nResponse:" ) # title
    print ( response['json_data_pretty'] ) # make look pretty for cli

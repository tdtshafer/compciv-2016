import requests
import json

def geocode(location):
    """
    Geocodes user-input varible location using Mapzen Search API

    What it expects:
    ----------------
    The "location" string, like "Stanford, CA"

    It also expects the variable `CREDS_FILE` to point to an existing file
    that contains a valid Mapzen Search key.

    What it does:
    -------------
    It opens and reads the file at CREDS_FILE to get the API key.

    It calls the Mapzen Search API via an HTTP request, using the API key, 
    and the user-provided "location" string as the "text" parameter.

    It deserializes the Mapzen Search response into a dictionary, using
    the JSON library that we can sort through

    It then creates a dictionary that we use to display the user's desired response

    What it returns:
    ----------------
    A dictionary containing these key-value pairs:

    - query_text: the "location" string provided by the user
    - label: The string label that Mapzen provides in describing the found location
    - confidence: A float representing the confidence value that Mapzen has in its result.
    - latitude: a float representing the latitude coordinate
    - longitude: a float representing the longitude coordinate
    - status: "OK", a string that indicates a result was found. Else, None

    """
    
    rawtext = fetch_mapzen_response(location)
    mydict = parse_mapzen_response(rawtext)
    # add the location string to mydict
    mydict['query_string'] = location 
    # return the diccionary
    return mydict
  
def fetch_mapzen_response(location):
    """
    
    getting the results from the awesome mapzen service
    
    `location` is a string that will be passed onto Mapzen API for geocoding

    returns a text string containing JSON-formatted data from Mapzen
    
    """
    MAPZEN_ENDPOINT = 'https://search.mapzen.com/v1/search'
    mykey = read_mapzen_credentials()
    my_params = {'api_key': read_mapzen_credentials(), 'text': location}
    resp = requests.get(MAPZEN_ENDPOINT, params = my_params)
    return resp.text


def parse_mapzen_response(txt):
    """
    `txt` is a string containing JSON-formatted text from Mapzen's API

    returns a dictionary containing the useful key/values from the most
       relevant result.
    """
    gdict = {} # just initialize a dict for now, with status of None
    data = json.loads(txt)
    if data['features']: # it has at least one feature...
        gdict['status'] = 'OK' 
        feature = data['features'][0] # pick out the first one
        props = feature['properties']  # just for easier reference
        gdict['confidence'] = props['confidence']
        gdict['label'] = props['label']

        # now get the coordinates
        coords = feature['geometry']['coordinates']
        gdict['longitude'] = coords[0]
        gdict['latitude'] = coords[1]
    else:
        gdict['status'] = None

    return gdict

def read_mapzen_credentials():
    creds_filename = "creds_mapzen.txt"
    keytxt = open(creds_filename).read().strip() # e.g. "search-blahblah"
    return keytxt  

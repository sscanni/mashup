from getAPIKeys import getAPIKey
import httplib2
import json

def getGeocodeLocation(inputString):

    apptab = getAPIKey("Google", "GeocodeLocation")
    if apptab.key1 == 'google_api_key':
       google_api_key = apptab.value1
    else:
        print ("Fatal Error accessing api key database")
        return None

    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)

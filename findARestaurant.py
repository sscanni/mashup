from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "HBTOFBMQOZZMJJWEY1YEDGEPJNPAEIC0DRQRWGA5SLGO3RL3"
foursquare_client_secret = "PSDEBLDRXIQRQVZKY23FTOWNQSHK5FIJAZC1N4IK12WTBDEY"

curdate = '20181023'

def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    latlong = getGeocodeLocation(location)
    latitude=('{:3.2f}'.format(latlong[0]))
    longitude=('{:3.2f}'.format(latlong[1]))
    latlong = ("%s,%s" % (latitude, longitude))
    #2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=%s&ll=%s&query=%s'% (foursquare_client_id, foursquare_client_secret, curdate, latlong, mealType))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    if result['response']['venues']:
        #3. Grab the first restaurant
        name = result['response']['venues'][0]['name']
        venue_id = result['response']['venues'][0]['id']
        addrLine = ""
        for i in result['response']['venues'][0]['location']['formattedAddress']:
            addrLine += i
            addrLine += " "
	    #4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture        
        url = ('https://api.foursquare.com/v2/venues/%s/photos/?client_id=%s&client_secret=%s&v=%s'% (venue_id, foursquare_client_id, foursquare_client_secret, curdate))
        h = httplib2.Http()
        result = json.loads(h.request(url,'GET')[1])
        #5. Grab the first image
        ImageURL = ""
        if result['meta']['code'] == '200':
            if result['response']['photos']['count'] > 0:
                ImageURL += result['response']['photos']['items'][0]['prefix']
                ImageURL += "300x300"
                ImageURL += result['response']['photos']['items'][0]['suffix']
            else:
                #6. If no image is available, insert default a image url
                ImageURL = "https://pixabay.com/en/restaurant-wine-glasses-served-449952/"
        else:
            ImageURL = "https://pixabay.com/en/restaurant-wine-glasses-served-449952/"
        #7. Return a dictionary containing the restaurant name, address, and image url	
        dict = {}
        dict['name'] = name
        dict['address'] = addrLine
        dict['imageurl'] = ImageURL
        return dict
    else: 
        return None
    
def PrintInfo(d):
    if d:
        print ("Restaurant Name: %s" % (d['name']))
        print ("Restaurant Address: %s" % (d['address']))
        print ("Imaage: %s" % (d['imageurl']))
        print 
    else:
        print ("No restaurants found")
    return

if __name__ == '__main__':
    PrintInfo(findARestaurant("Pizza", "Tokyo, Japan"))
    PrintInfo(findARestaurant("Tacos", "Jakarta, Indonesia"))
    PrintInfo(findARestaurant("Tapas", "Maputo, Mozambique"))
    PrintInfo(findARestaurant("Falafel", "Cairo, Egypt"))
    PrintInfo(findARestaurant("Spaghetti", "New Delhi, India"))
    PrintInfo(findARestaurant("Cappuccino", "Geneva, Switzerland"))
    PrintInfo(findARestaurant("Sushi", "Los Angeles, California"))
    PrintInfo(findARestaurant("Steak", "La Paz, Bolivia"))
    PrintInfo(findARestaurant("Gyros", "Sydney Australia"))

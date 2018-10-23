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
    # print (latlong)    
    latitude=('{:3.2f}'.format(latlong[0]))
    longitude=('{:3.2f}'.format(latlong[1]))
    latlong = ("%s,%s" % (latitude, longitude))
    # print (latlong)
	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=%s&ll=%s&query=%s'% (foursquare_client_id, foursquare_client_secret, curdate, latlong, mealType))
#    print (url)
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    # print (result)
    if result['response']['venues']:
        print ("--------------------------------------------------------------------------")
        # print (result['response']['venues'][0])
        print (result['response']['venues'][0]['name'])
        print (result['response']['venues'][0]['id'])
        # print (result['response']['venues'][0]['location']['formattedAddress'][0])
        # print (result['response']['venues'][0]['location']['formattedAddress'][1])
        addrLine = ""
        for i in result['response']['venues'][0]['location']['formattedAddress']:
            addrLine += i
            addrLine += " "
        if addrLine:
            print (addrLine)

        # print (result['response']['venues'][0]['location']['city'])
        # print (result['response']['venues'][0]['location']['state'])
        # print (result['response']['venues'][0]['location']['country'])
        # print (result['response']['venues'][0]['categories'][0]['icon']['prefix'])
        # print (result['response']['venues'][0]['categories'][0]['icon']['suffix'])

        # print (result)
        # latitude = result['results'][0]['geometry']['location']['lat']
        # longitude = result['results'][0]['geometry']['location']['lng']
        #print (result)
    return result
	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url	



if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")

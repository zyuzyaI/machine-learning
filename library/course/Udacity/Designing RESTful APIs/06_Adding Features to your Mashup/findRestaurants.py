from geopy.geocoders import Nominatim 
import requests 
import config
import json 

URL = "https://api.foursquare.com/v2/venues/search"

param = {
    "client_id": config.client_id,
    "client_secret": config.client_secret,
    "v": 20200409
}

def findRestaurant(category, place):
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    loc = geolocator.geocode(place)
    latitude = loc.latitude
    longitude = loc.longitude

    param["query"] = category
    param["ll"] = "%s, %s" %(latitude,  longitude)

    response = requests.get(URL, params=param).text
    response_json = json.loads(response)

    if response_json["response"]["venues"]:
        restaurant = response_json["response"]["venues"][0]
        venue_id = restaurant['id'] 
        restaurant_name = restaurant["name"]
        restaurant_address = restaurant['location']['formattedAddress']
        #Format the Restaurant Address into one string
        address = ""
        for i in restaurant_address:
            address += i.casefold() + " "
        restaurant_address = address

        # get photo
        url_photo = "https://api.foursquare.com/v2/venues/%s/photos" % venue_id
        param["query"] = None
        param["ll"] = None
        result = requests.get(url_photo, params=param).text
        result = json.loads(result)
        try:
            if result['response']['photos']['items']:
                    firstpic = result['response']['photos']['items'][0]
                    prefix = firstpic['prefix']
                    suffix = firstpic['suffix']
                    imageURL = prefix + "300x300" + suffix
            else:
                imageURL = "https://www.pnp.ru/upload/entities/2018/10/29/article/detailPicture/74/76/da/5f/29aa36ef39fae0c94d366b2299c30e39.jpg" 
        except:
            imageURL = "https://www.pnp.ru/upload/entities/2018/10/29/article/detailPicture/74/76/da/5f/29aa36ef39fae0c94d366b2299c30e39.jpg" 
        
        restaurantInfo = {'name':restaurant_name, 'address':restaurant_address, 'image':imageURL}
        
        return restaurantInfo
    else:
        return "No Restaurants Found"

if __name__ == "__main__":
    print(findRestaurant("Pizza", "Tokyo, Japan"))
    findRestaurant("Tacos", "Jakarta, Indonesia")
    findRestaurant("Tapas", "Maputo, Mozambique")
    findRestaurant("Falafel", "Cairo, Egypt")
    findRestaurant("Spaghetti", "New Delhi, India")
    findRestaurant("Cappuccino", "Geneva, Switzerland") 
    findRestaurant("Sushi", "Los Angeles, California")
    findRestaurant("Steak", "La Paz, Bolivia")
    findRestaurant("Gyros", "Sydney, Australia")


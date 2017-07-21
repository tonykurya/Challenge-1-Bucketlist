import googlemaps   #Python client library for Google Maps API WEB Services

def decodeLocation():
    userLocation = input("Enter city: ")
    if isinstance(userLocation, str):
        pass
    else:
        raise TypeError('Input must be a string')

    gmaps = googlemaps.Client(key='AIzaSyAh-fJo9iivUrpntTXP1f9vt5ILSNHH32E')
    # Geocoding an address
    geocode_result = gmaps.geocode(userLocation, {"country": "KE"})
    result = geocode_result[0]['geometry']['location']
    hospitals_nearby = gmaps.places('Hospital', result, 500)
    print(places_nearby)


decodeLocation()


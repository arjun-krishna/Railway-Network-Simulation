import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCyNhGhbKpgCvxE-isEtksti__YqKDqOF8')
def get_geocode_station(station_name):
	# Geocoding an address
	geocode_result = gmaps.geocode(station_name)[0]
	# print geocode_result
	return (geocode_result['geometry']['location']['lat'],geocode_result['geometry']['location']['lng'])

# test
get_geocode_station('chennai')

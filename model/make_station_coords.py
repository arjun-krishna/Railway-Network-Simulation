import csv
from geocode_stations import get_geocode_station
stationlist = []
with open('stations.csv') as f:
	reader = csv.reader(f)
	for row in reader:
	    stationlist.append((row[0], row[1]))


print len(stationlist)

with open('station_coords.csv', 'w') as csvfile:
	fieldnames = ['id', 'name', 'code', 'latitude', 'longitude']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()
	index = 1
	for row in stationlist:
		try :
			
			station_name=row[1]
			# if "Jn" in station_name:
			# 	station_name = station_name.rsplit(' ', 1)[0]
			print index, station_name
			coords = get_geocode_station(station_name)
			writer.writerow({'id':index, 'name': row[1], 'code': row[0],'latitude':coords[0], 'longitude':coords[1]})
			index += 1
		except :
			writer.writerow({'id':index, 'name': row[1], 'code': row[0],'latitude':'', 'longitude':''})
			index+= 1
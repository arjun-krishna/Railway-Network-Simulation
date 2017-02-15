import csv
from get_platform_no import get_platformnum_from_ir
from geocode_stations import get_geocode_station
stationlist = []
with open('stations.csv') as f:
	reader = csv.reader(f)
	for row in reader:
	    stationlist.append((row[0], row[1]))


print len(stationlist)

with open('stations_new.csv', 'w') as csvfile:
	fieldnames = ['id', 'name', 'code', 'latitude', 'longitude', 'platforms']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()
	index = 1
	for row in stationlist:
		try :
			print index, row[1]
			station_name=row[1]
			if "Jn" in station_name:
				station_name = station_name.rsplit(' ', 1)[0]
			no_platforms = get_platformnum_from_ir(station_name)
			coords = get_geocode_station(station_name)
			writer.writerow({'id':index, 'name': row[1], 'code': row[0],'latitude':coords[0], 'longitude':coords[1], 'platforms':no_platforms})
			index += 1
		except :
			writer.writerow({'id':index, 'name': row[1], 'code': row[0],'latitude':'', 'longitude':'', 'platforms':-1})
			index+= 1
import csv
from get_platform_no import get_platformnum_from_ir
stationlist = []
with open('stations.csv') as f:
	reader = csv.reader(f)
	for row in reader:
	    stationlist.append((row[0], row[1]))


print len(stationlist)

with open('station_platformno.csv', 'w') as csvfile:
	fieldnames = ['id', 'name', 'code', 'platforms']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()
	index = 1
	for row in stationlist:
		try :
			print index, row[1]
			station_name=row[1]
			if "Jn" in station_name:
				station_name = station_name.rsplit(' ', 1)[0]
			platform_data = get_platformnum_from_ir(station_name)
			no_platforms = -2
			if 'error' not in platform_data:
				no_platforms = platform_data['data']
			writer.writerow({'id':index, 'name': row[1], 'code': row[0],'platforms':no_platforms})
			index += 1
		except :
			writer.writerow({'id':index, 'name': row[1], 'code': row[0],'platforms':-1})
			index+= 1
import requests 
from bs4 import BeautifulSoup as BS

num = int(raw_input('Enter Train number'))

r = requests.get('http://indiarailinfo.com/shtml/list.shtml?LappGetTrainList/'+str(num)+'/0/0/0?')
fbs = BS(r.text, 'html.parser')
table = fbs.findAll('table')
if len(table) > 0 and int(table[0].attrs['numrows']) == 1: 
	tr = table[0].tr
	num = tr.findAll('td')[0].string
	r = requests.get('http://indiarailinfo.com/train/timetable/all/' + str(num))
	bs = BS(r.text, 'html.parser')
	table = bs.findAll('table', {'class':'newschtable'})
	station_list = []
	failed_list = []
	if len(table) > 0 :
		table = table[0]
		trows = table.findAll('tr')
		for row in trows:
			if not row.has_attr('style'):
				continue
			tds = row.findAll('td')
			station_data = {}
			if len(tds) > 3 and tds[3].a:
				data = tds[3].a['title']
				step1 = data.split('|')[0]
				station_data['st_name'] = step1.split('/')[1].split('(')[0]
				# station_data['platform_count'] = int(data.ssplit('(')[1].split(' ')[0])
				
				if "(" in step1 :
					station_data['platform_count'] = int(step1.split('(')[1].split(' ')[0])
				else :
					failed_list.append(station_data['st_name'])
			if len(tds) > 2 and tds[2].a:
				station_data['st_code'] = tds[2].a.string
			# if row.has_attr('class'):
				# print row.attrs['class']
			if row.has_attr('class') and 'substn' in row.attrs['class'] :
				station_data['is_substation'] = True
			else :
				station_data['is_substation'] = False
			station_list.append(station_data)

	for station_data in station_list:
		if station_data['st_name'] not in failed_list:
			print station_data['is_substation'], station_data['st_code'], station_data['st_name'], station_data['platform_count']
		else :
			print 'This has no platform count : ', station_data['st_name']
		# pass

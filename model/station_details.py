"""
Objective :
Get Number of platforms given a station 
"""
from bs4 import BeautifulSoup
import urllib2
import re
import csv

def search(query) :
	q = urllib2.quote(query,safe='')
	url = 'http://www.bing.com/search?q='+q
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0') 
	response = urllib2.urlopen(req)
	page = response.read()
	# print page
	return BeautifulSoup(page)

# page = urllib2.urlopen(site).read()
# soup = BeautifulSoup(page)
# print soup.prettify()

# soup = search('indiarailinfo arrivals '+'SINGARAM')
# print soup.findAll('a', href=re.compile('^http://indiarailinfo.com/arrivals/'))[0]['href']


arrival_regex = re.compile('^http://indiarailinfo.com/arrivals/')

with open('stations.csv', 'rb') as f:
		reader = csv.reader(f)
		flag = False
		for row in reader:
			soup = search('indiarailinfo arrivals '+row[1])
			try :
				station_code = re.compile('-'+row[0].lower().split(' ')[0])
				links = map(lambda x: x['href'],soup.findAll('a', href=arrival_regex))
				link = 'NULL'
				for e in links :
					if station_code.search(e) :
						link = e

			except :
				link = 'NULL'

			print row[0],' , ', row[1],' , ', link
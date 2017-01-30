"""
Wikipedia Indian Railway stations
"""
from bs4 import BeautifulSoup
import urllib2

site = 'https://en.wikipedia.org/wiki/List_of_railway_stations_in_India'

page = urllib2.urlopen(site).read()
soup = BeautifulSoup(page)


codes = []

for table in soup.find_all('table') :
	for tr in table.find_all('tr')[1:] :
		tds = tr.find_all('td')
		platform = 'null'
		if (tds != None) :
			a = tds[0].find_all('a')
			if (a != None) :
				try :
					a = a[0]
					if a.has_attr('class') and a['class'][0] == 'new':
						pass
					else :
						platform = get_platform('https://en.wikipedia.org'+a['href'])
				except IndexError :
					pass
			try :
				if (len(tds[1].text)) :
					codes.append(tds[1].text)
			except IndexError :
				pass


for code in codes :
	print code

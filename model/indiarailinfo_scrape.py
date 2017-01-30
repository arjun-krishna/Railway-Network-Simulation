# http://indiarailinfo.com/arrivals/9495

from bs4 import BeautifulSoup,  NavigableString
import urllib2

def parse_text(text) :
	# 'Arrivals at HWH/Howrah Junction (23 PFs)'
	text = text[12:]
	L = []
	try :
		s = text.split('(')
		L += s[0].split('/')
		L.append(s[1].split('PFs')[0])
		return ','.join(L)
	except Exception :
		return text
site = 'http://indiarailinfo.com/arrivals/'

f = open('station_info.csv','a')
SITES = 9496
CHECK_POINT = 10
for i in range(1,9496) :
	page = urllib2.urlopen(site+str(i)).read()
	soup = BeautifulSoup(page)

	data = soup.find_all('h1')[0]
	text = [element for element in data if isinstance(element, NavigableString)]
	f.write(parse_text(text[0])+'\n')
	if (i%CHECK_POINT == 0) :
		print (i*100.0)/SITES


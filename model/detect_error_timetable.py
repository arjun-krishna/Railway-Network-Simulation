"""
given : isl_wise_train_detail_03082015_v1.csv [ Indian Railways timetable csv ]

output : A list of all the trains and the route of the train [ represented as json ]
"""

import csv
import json

"""
0  - Train No.
1  - train Name  
2  - islno 
3  - station Code  
4  - Station Name  
5  - Arrival time  
6  - Departure time  
7  - Distance  
8  - Source Station Code 
9  - source Station Name 
10 - Destination station Code  
11 - Destination Station Name
"""

trains = {}
error = set()
with open('train_data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        try :
          x = trains[row[0]+row[1]][row[2]] 
          error.add(row[0])
        except Exception : 
          trains[row[0]+row[1]] = {row[2]:0}
        

for train_no in error :
  print train_no

print len(error)

"""
'12488'
'19713'
'18504'
'13153'
'15909'
'12945'
'59076'
'13352'
'12906'
'12147'
'17205'
'01156'
'17401'
'06542'
'59386'
'18110'
'15013'
'58220'
'11063'
'12972'
'18408'
'11039'
'13345'
'58114'
'16688'
'12343'
'19711'
'12780'
'17222'
'59207'
'22936'
'18241'
'19580'
'12463'
'11040'
'19005'
'22651'
'17603'
'14265'
'15632'
'13131'
'59441'
'12971'
'12448'
'06541'
'13009'
'18238'
'11037'
'19203'
'59230'
'12925'
'18010'
'14041'
'12941'
'05010'
'14659'
'21028'
'12687'
'12995'
'08891'
'13008'
'18048'
'24370'
'18235'
'18452'
'11057'
'14887'
'59272'
'19204'
'11067'
'59208'
'12307'
'18181'
'22133'
'12139'
'15308'
'11051'
'18302'
'11019'
'12942'
'13141'
'19311'
'12149'
'17226'
'12722'
'19260'
'15035'
'12946'
'18623'
'14370'
'12719'
'15018'
'14163'
'19259'
'56909'
'22935'
'14511'
'16318'
"""
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
with open('isl_wise_train_detail_03082015_v1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        try :
          trains[row[0]]['route'].append(row[3])
          trains[row[0]]['distance'].append(row[7])
          trains[row[0]]['arrival'].append(row[5])
          trains[row[0]]['departure'].append(row[6])
        except Exception : 
          trains[row[0]] = {'train_id': row[0],'name':row[1],'src':row[8],'dst':row[10],'route' : [],'distance':[],'arrival':[],'departure':[]}
          trains[row[0]]['route'].append(row[3])
          trains[row[0]]['distance'].append(row[7])
          trains[row[0]]['arrival'].append(row[5])
          trains[row[0]]['departure'].append(row[6])

        
L = []

for train_no in trains :
  L.append(trains[train_no])

print json.dumps(L,indent=4, separators=(',', ': '))
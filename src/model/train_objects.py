#!/usr/bin/python
"""
module : train_objects
description :
Takes in the train timetable dataset and converts it into a suitable json object
for easier extraction of the network and other details.

IO 
----
input  : isl_wise_train_detail_03082015_v1.csv [ Indian Railways timetable csv ]

output : A list of all the trains and the route of the train [ represented as json ]
"""

import csv
import json
import sys

"""
TimeTable dataset features
----------------------------
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

# Error detection phase
trains = {}
error = set()
total_trains = set()
with open('../data/isl_wise_train_detail_03082015_v1.csv') as f:
    reader = csv.reader(f)
    isHeader = True
    for row in reader:
        if isHeader :
          isHeader = False
          continue
        try :
          x = trains[row[0]+row[1]][row[2]] 
          error.add(row[0]+row[1])
        except Exception : 
          trains[row[0]+row[1]] = {row[2]:0}
          total_trains.add(row[0]+row[1])

# Output detected errors
sys.stderr.write("# errors : "+str(len(error))+"\n")
sys.stderr.write("# trains : "+str(len(total_trains))+"\n")

# Extraction code
trains = {}
with open('../data/isl_wise_train_detail_03082015_v1.csv') as f:
    reader = csv.reader(f)
    isHeader = True
    for row in reader:
        if isHeader :
          isHeader = False
          continue
        if (row[0]+row[1]) in error :   # skip processing error detected trains in data
          continue
        try :
          trains[row[0]+row[1]]['route'].append(row[3])
          trains[row[0]+row[1]]['distance'].append(row[7])
          trains[row[0]+row[1]]['arrival'].append(row[5])
          trains[row[0]+row[1]]['departure'].append(row[6])
        except Exception : 
          trains[row[0]+row[1]] = {'train_id': row[0],'name':row[1],'src':row[8],'dst':row[10],'route' : [],'distance':[],'arrival':[],'departure':[]}
          trains[row[0]+row[1]]['route'].append(row[3])
          trains[row[0]+row[1]]['distance'].append(row[7])
          trains[row[0]+row[1]]['arrival'].append(row[5])
          trains[row[0]+row[1]]['departure'].append(row[6])

        
L = []

for train_id in trains :
  L.append(trains[train_id])

print json.dumps(L,indent=4, separators=(',', ': '))  
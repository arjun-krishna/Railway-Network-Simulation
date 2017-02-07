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
with open('isl_wise_train_detail_03082015_v1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        try :
          x = trains[row[0]][row[2]] 
          error.add(row[0])
        except Exception : 
          trains[row[0]] = {row[2]:0}
        
for train_no in error :
  print train_no
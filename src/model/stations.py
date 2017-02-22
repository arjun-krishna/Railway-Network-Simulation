#!/usr/bin/python
"""
module : stations
description : 
Get the station codes of the nodes in the network
IO
---
input  : network_edgL [ from rail_network.py output ]

output : List of station codes
"""

import csv 

stations = set()

with open('../data/network_edgL') as f:
    reader = csv.reader(f)
    for row in reader:
      stations.add(row[0])
      stations.add(row[1])

stations = list(stations)
stations.sort()
for station in stations :
	print station


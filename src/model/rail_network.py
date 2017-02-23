#!/usr/bin/python
"""
module : rail_network
description : 
Prints the railway network in the form of edge list.

IO
---
input  : trains_data.json [ from train_objects.py output ]

output : edge list of the network.
"""

import json

def clean_up(string) :
    return string.replace(" ", "")

edges = set()

with open('../data/trains_data.json') as json_data:
    trains = json.load(json_data)
    json_data.close()

    for train in trains :
      for i in xrange(len(train["route"])-1) :
        edge = (clean_up(train["route"][i]),clean_up(train["route"][i+1]))
        edges.add(edge)
    edges = list(edges)
    edges.sort()

    for edge in edges :
      print ("%s, %s" %(edge[0],edge[1]))


"""
description : prints the railway network

output : edge list , distance is an attribute of the edge
"""

import json

edges = set()

with open('trains.json') as json_data:
    trains = json.load(json_data)
    json_data.close()

    for train in trains :
      for i in xrange(len(train["route"])-1) :
        edge = (train["route"][i],train["route"][i+1],(int(train["distance"][i+1]) - int(train["distance"][i]) ))
        edges.add(edge)
    edges = list(edges)
    edges.sort()

    for edge in edges :
      print ("%s, %s, %d" %(edge[0],edge[1],edge[2]))


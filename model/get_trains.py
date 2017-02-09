"""
given : isl_wise_train_detail_03082015_v1.csv [ Indian Railways timetable csv ]

output : A list of all the trains in the dataset
"""

import csv

S = set()
with open('isl_wise_train_detail_03082015_v1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        S.add((row[0],row[1]))

for elem in S :
	print elem[0], " , ",elem[1]
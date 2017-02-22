#!/usr/bin/python
"""
module : station_location
description :
Takes in the train timetable dataset proc [ processed by Sachin Sridhar's team for their CNA project,
with some updates from me ] and outputs the station code to location map [json]

IO 
----
input  : Train_details_proc.csv [ Indian Railways timetable processed csv ]

output : map station code to location [ represented as json ]
"""

import csv
import json
import sys


station_location = {}
with open('../data/Train_details_proc.csv') as f:
    reader = csv.reader(f)
    isHeader = True
    for row in reader:
        if isHeader :
          isHeader = False
          continue
        try :
          station_location[row[3]]
        except Exception :
          if ((row[5] == '-1') or (row[6] == '-1' )):
            sys.stderr.write(row[3]+" -- "+row[4]+"\n") 
          station_location[row[3]] = {
            "lat" : row[5],                    # N/S
            "lng" : row[6]                     # E/W
          }


print json.dumps(station_location,indent=4, separators=(',', ': '))  
"""
MHAD -- MOHADI PRGN LNG  -- 21.236314, 76.042643
ANKX -- ANK MMR DIRECT   -- 20.182332, 74.454550
SGAM -- SAREIGRAM        -- 24.021264, 82.177776
KCV -- KRISHNA CH PURA   -- 21.851022, 86.802935
AYRN -- AKSHAYWAT R NGR  -- 25.654395, 85.317517
TKBG -- TEKKABIGHA       -- 25.464989, 85.488735
MMKB -- MEKRA MEMERKHAB  -- 25.4719147,85.8276422
MZM -- MUZZAMPUR NRYN    -- 29.609595, 78.290963
MKRH -- MALLICKPUR HAT   -- 25.871420, 87.837435
SDBH -- SINDRIBLOCK HUT  -- 23.610664, 85.280324
PQN -- PARIAWAN K.K.RD   -- 25.847285, 81.334910
VNE -- VISWANATH CHRLI   -- 26.770132, 93.165803
KKPM -- KALLAKKUDI PLGH  -- 10.919545, 78.887111
SBBJ -- SBB JOGULAMBA H  -- 16.228764, 77.811715
GHPU -- GANDHIPURAM HAL  -- 17.494646, 80.313419
UDM -- UNDASA MADHAWPU   -- 23.070190, 75.972218
SPDR -- SHEOPRASADNAGER  -- 23.310117, 82.770332
GADH -- GOALDIH          -- 21.726588, 85.547688
KPRR -- KOTAPAR ROAD     -- 19.040456, 82.307767
SNC -- SNARAYAN CHAPIA   -- 26.980317, 82.395508
DGPP -- DHENGLI PP GOAN  -- 19.392432, 76.499033
"""
"""
GGB -- GARHMUKTESAR BR -- 28.48,78.06 
BSS -- BAHADUR SINGH W -- 30.3085636,75.8525483 
NJM -- N J RAMANAL -- 15.2130497,75.018999 
LGB -- LOHGARH ABUB -- 30.6451636,76.8079271 
KRSH -- KARAMGARH SDRGH -- 29.9554536,75.1120285 
UAR -- UNAWA AITHOR -- 23.7684951,72.3498009 
GLNA -- GOLANA HALT -- 24.8444901,72.3651612 
PPH -- PIPRI DIH -- 24.2029038,83.0168307 
PSPY -- PRASANNAYANAPAL -- 14.6495639,77.5929273 
KUG -- KUSUGALI -- 15.3962383,75.2031969 
THKU -- THALLAK -- 14.5693155,76.7844102 
HAQ -- HASTAVARAMU -- 14.2194173,79.1194118 
PDO -- POODOOR -- 16.5853813,81.7431948 
INK -- INTEKANNE -- 17.7281623,79.8593402 
MMPR -- MAMDAPUR HALT -- 18.8221475,78.1263055
NKX -- NAKTISEMRA -- 19.0663951,82.0830302 
KMEZ -- KUMHAR MARENGA -- 21.2482323,81.498798 
UIH -- UMARIA ISPA HLT -- 23.6236519,80.3826041 
MQQ -- MARKAHANDI U HT -- 22.049068,79.1782083 
CRE -- CHORGHATPIPARIA -- 23.0363649,79.9190113 
JONR -- JEONARA PH -- 22.4644195,80.0820574 
BRDH -- BARDHANA HALT -- 21.8842784,85.7357502 
BAGD -- BAGWADA (HALT) -- 20.4358708,72.9053076 
WSE -- VASAN IYAWA -- 20.8153483,72.9416637 
"""

"""
CEM -- CHEKATE G PALEM -- 16.0095878,79.6840524
JBK -- JGMBLA KSHNPRM -- 15.5231205,79.0659303
KSTE -- KISTAMSETIPALLI -- 15.3656971,78.8777803
KEF -- KRISHNAMMAKONA -- 15.486505,78.1929803
SVPM -- S VENKTESWRPALM -- 14.8028077,79.9736559
PAVP -- P AVATAPALLE -- 16.5548562,80.8317014
PSX -- PTNSNGI TWN HLT -- 21.3453102,79.0077442
MGTD -- MEGHPURTITODI -- 22.1398708,69.4548958
GGM -- GORA GHUMA -- 23.0233738,72.3666645
MDLM -- MUNDALARAM -- 23.7445954,75.1378154
URML -- UPARMAL -- 25.2468696,75.2697341
PRDH -- PIRDULESHA HALT -- 25.9216552,72.9655638
"""
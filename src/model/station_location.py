#!/usr/bin/python
"""
module : station_location
description :
Takes in the train timetable dataset proc [ processed by Sachin Sridhar's team for their CNA project]
and outputs the station code to location map [json]
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
MHAD -- MOHADI PRGN LNG
ANKX -- ANK MMR DIRECT
SGAM -- SAREIGRAM
KCV -- KRISHNA CH PURA
AYRN -- AKSHAYWAT R NGR
TKBG -- TEKKABIGHA
MMKB -- MEKRA MEMERKHAB
MZM -- MUZZAMPUR NRYN
MKRH -- MALLICKPUR HAT
SDBH -- SINDRIBLOCK HUT
PQN -- PARIAWAN K.K.RD
VNE -- VISWANATH CHRLI
KKPM -- KALLAKKUDI PLGH
SBBJ -- SBB JOGULAMBA H
GHPU -- GANDHIPURAM HAL
UDM -- UNDASA MADHAWPU
SPDR -- SHEOPRASADNAGER
GADH -- GOALDIH
KPRR -- KOTAPAR ROAD
SNC -- SNARAYAN CHAPIA
DGPP -- DHENGLI PP GOAN
GGB -- GARHMUKTESAR BR
BSS -- BAHADUR SINGH W
NJM -- N J RAMANAL
LGB -- LOHGARH ABUB
KRSH -- KARAMGARH SDRGH
PRDH -- PIRDULESHA HALT
UAR -- UNAWA AITHOR
GLNA -- GOLANA HALT
PPH -- PIPRI DIH
CEM -- CHEKATE G PALEM
JBK -- JGMBLA KSHNPRM
KSTE -- KISTAMSETIPALLI
KEF -- KRISHNAMMAKONA
PSPY -- PRASANNAYANAPAL
KUG -- KUSUGALI
THKU -- THALLAK
SVPM -- S VENKTESWRPALM
PAVP -- P AVATAPALLE
HAQ -- HASTAVARAMU
PDO -- POODOOR
INK -- INTEKANNE
MMPR -- MAMDAPUR HALT
NKX -- NAKTISEMRA
KMEZ -- KUMHAR MARENGA
PSX -- PTNSNGI TWN HLT
UIH -- UMARIA ISPA HLT
MQQ -- MARKAHANDI U HT
CRE -- CHORGHATPIPARIA
JONR -- JEONARA PH
MGTD -- MEGHPURTITODI
BRDH -- BARDHANA HALT
BAGD -- BAGWADA (HALT)
GGM -- GORA GHUMA
WSE -- VASAN IYAWA
MDLM -- MUNDALARAM
URML -- UPARMAL
"""
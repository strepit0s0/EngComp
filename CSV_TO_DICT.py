### Trasform CSV in Dict

import csv

## GERMANY
Germany = open("germany-latest.csv", "r", encoding="utf-8") #open file
fieldnames = ("Category","OSM - id","Latitude","Longitude","Place")
reader = csv.DictReader(Germany, fieldnames, delimiter = "|")
germany_list =[]
for line in reader:
    germany_list.append(line)

for i in range(len(germany_list)):
    germany_list[i] = dict(germany_list[i].items()) 

for i in range(len(germany_list)):
    germany_list[i]["Category"] = int(germany_list[i]["Category"])
    germany_list[i]["Latitude"] = float(germany_list[i]["Latitude"])
    germany_list[i]["Longitude"] = float(germany_list[i]["Longitude"]) #transform value in interger, float...

Germany.close()
	
## ITALY
italy = open("italy-latest.csv", "r", encoding="utf-8") #open file
fieldnames = ("Category","OSM - id","Latitude","Longitude","Place")
reader = csv.DictReader(italy, fieldnames, delimiter = "|")
italy_list =[]
for line in reader:
    italy_list.append(line)

for i in range(len(italy_list)):
    italy_list[i] = dict(italy_list[i].items()) 

for i in range(len(italy_list)):
    italy_list[i]["Category"] = int(italy_list[i]["Category"])
    italy_list[i]["Latitude"] = float(italy_list[i]["Latitude"])
    italy_list[i]["Longitude"] = float(italy_list[i]["Longitude"]) #transform value in interger, float...

italy.close()

## SPAIN

Spain = open("spain-latest.csv", "r", encoding="utf-8") #open file
fieldnames = ("Category","OSM - id","Latitude","Longitude","Place")
reader = csv.DictReader(Spain, fieldnames, delimiter = "|")
spain_list =[]
for line in reader:
    spain_list.append(line)

for i in range(len(spain_list)):
    spain_list[i] = dict(spain_list[i].items()) 

for i in range(len(spain_list)):
    spain_list[i]["Category"] = int(spain_list[i]["Category"])
    spain_list[i]["Latitude"] = float(spain_list[i]["Latitude"])
    spain_list[i]["Longitude"] = float(spain_list[i]["Longitude"]) #transform value in interger, float...

Spain.close()


## FRANCE
France = open("france-latest.csv", "r", encoding="utf-8") #open file
fieldnames = ("Category","OSM - id","Latitude","Longitude","Place")
reader = csv.DictReader(France, fieldnames, delimiter = "|")
france_list =[]
for line in reader:
    france_list.append(line)

for i in range(len(france_list)):
    france_list[i] = dict(france_list[i].items()) 

for i in range(len(france_list)):
    france_list[i]["Category"] = int(france_list[i]["Category"])
    france_list[i]["Latitude"] = float(france_list[i]["Latitude"])
    france_list[i]["Longitude"] = float(france_list[i]["Longitude"]) #transform value in interger, float...

France.close()


## GREAT-BRITAIN
GB = open("great-britain-latest.csv", "r", encoding="utf-8") #open file
fieldnames = ("Category","OSM - id","Latitude","Longitude","Place")
reader = csv.DictReader(GB, fieldnames, delimiter = "|")
gb_list =[]
for line in reader:
    gb_list.append(line)

for i in range(len(gb_list)):
    gb_list[i] = dict(gb_list[i].items()) 

for i in range(len(gb_list)):
    gb_list[i]["Category"] = int(gb_list[i]["Category"])
    gb_list[i]["Latitude"] = float(gb_list[i]["Latitude"])
    gb_list[i]["Longitude"] = float(gb_list[i]["Longitude"]) #transform value in interger, float...

GB.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:28:02 2018

@author: noramariamititelu
"""

import json
import csv 

with open ('conflict_data/conflict_data_full_lined.json') as file:
    conflict_data = json.load(file)

# Import the JSON and CSV packages


# Load in the conflict JSON data
#with open('conflict_data.json') as file:
#    data = json.load(file)

# Open the output CSV file we want to write to

    # Actually write the data to the CSV file here.
    # You can use the same csvwriter.writerow command to output the data 
    #   as is used above to output the headers.
    
Brazil = []
for country in conflict_data:
    if country ["country"] == "Brazil" :
        Brazil.append(country)

# new empty list of Brazil, containing the data with the item country as Brazil
# You append the country to the new empty list Brazil 
        
Colombia = []
for country in conflict_data : 
    if country ["country"] == "Colombia": 
        Colombia.append(country)

#same thing for Colombia, as I want to compare the 2 countries, both considered violent, 
# on the number of total deaths in the year 2004
        # I chose 2004 because I saw a big spike of conflicts in Colombia in 2004 
    

list_Brazil_2004 = []

for item in Brazil :
#    print (type(item ["year"]))
    if item["year"] == 2004:
        print (item)
        list_Brazil_2004.append(item)

# list with only the registries from 2004 in Braasil 

list_Colombia_2004 = []
for item in Colombia : 
    if item ["year"] == 2004:
        list_Colombia_2004.append (item) 
        
        
# list with only the registries from 2004 in Colombia, termed as conflicts         

unknown_deaths_Brazil = []
for item in list_Brazil_2004 :
    print (item["deaths_unknown"])
    unknown_deaths_Brazil.append(item["deaths_unknown"])




#unknown_deaths_Brazil = []
#for item in list_Brazil_2004 :
#    print (item["deaths_unknown"])
#    unknown_deaths_Brazil.append(item)

# I was actually trying to append the whole directory, not just the values of the unknown_deaths
# When I appended ("deaths_unknown"), it only showed the words "deaths_unknown", instead of showing the values
# SO you have to print the item ("deaths_unkown")
    







unknown_deaths_Colombia = []
for item in list_Colombia_2004: 
    print (item["deaths_unknown"])
    unknown_deaths_Colombia.append(item["deaths_unknown"])

# prints out the values in a separate list, containing the values for the unknown deaths 
# but for getting the sum of the total values for the deaths, no matter which deaths you
# want to look at, you try to use the total_deaths thing from earlier, with a value = 0 
    
total_deaths_Brazil = 0
for item in list_Brazil_2004 :
    total_deaths_Brazil += item ["best"]

total_deaths_Colombia = 0 
for item in list_Colombia_2004 :
    total_deaths_Colombia += item ["best"]
    
deaths_civilians_Brazil = 0 
for item in list_Brazil_2004:
    
    



with open('Brazil_data2004.csv', 'w', newline='') as file:
   csvwriter = csv.writer(file, delimiter =',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
   csvwriter.writerow(['country', 'year', 'longitude','latitude', 'source_original','conflict_name', 'best','type_of_violence','deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown'])
   for item in list_Brazil_2004:
         csvwriter = csv.writer(file, delimiter =',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
         csvwriter.writerow([item['country'], item ['year'],item['longitude'], item['latitude'],item['source_original'] item['conflict_name'], item['best'], item['type_of_violence'],item['deaths_a'], item['deaths_b'], item['deaths_civilians'], item['deaths_unknown']])   

# transforming the json files to csv files, to be able to work with them easier in R program 

with open ('Colombia_data2004.csv', 'w', newline='') as file:
    csvwriter = csv.writer(file, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['country', 'year', 'longitude', 'latitude', 'source_original','conflict_name', 'best','type_of_violence','deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown'])
    for item in list_Colombia_2004:
        csvwriter = csv.writer(file, delimiter =',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        csvwriter.writerow([item['country'], item ['year'], item ['longitude'], item['latitude'] , item['source_original'], item['conflict_name'], item['best'], item['type_of_violence'],item['deaths_a'], item['deaths_b'], item['deaths_civilians'], item['deaths_unknown']])   


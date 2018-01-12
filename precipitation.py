#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:54:11 2018

@author: noramariamititelu
"""

import json 
#loading json packages 

with open ('precipitation.json') as file :
    precipitation_data = json.load (file)
#open the precipitation data through json.load

monthly_precip = [0]*12 
#create a new list, for the montly precipitations, and you assign it 12 new empty places [0]*12, so
#basically a new list with twelve empty spots, which could take up any value 
#You do this to be able to assign the respective precipitations for each month to 

for dic in precipitation_data:
#you look through the entire data 
    if dic['station'] == 'GHCND:US1WAKG0038': 
        #if the item 'station' in this data set has this code 
        monthly_precip [int(dic['date'][5:7])-1] += dic['value'] 
#put in the newly created list (monthly_precip) the values of sum of the values of the months
# += adds the values from every month to the initial index (that is why it is [5:7] - 1, because to 
#look at the month you want, you need to look at the index 3-1 to see march). 
# and with += you just keep adding the values to the initial value, which was 0 
# the index is 5-7 because that was the index from the item 'date', at which you could find the month

yearly_total = sum(monthly_precip)
print('total yearly rainfall : ' + str(monthly_precip))  
# create new value, yearly_total with the sum of the monthly_precip 

for item in monthly_precip: 
    relative_monthly_precip = (item/yearly_total)
    print(relative_monthly_precip)
#for loop that just goes through the monthly precipitations and the relative values are the ones 


import json 

with open ('file.json', 'w') as file: 
    json.dump ({"Seattle": { 
        "totalYearlyPrecipitation" : yearly_total, 
        "totalMonthlyPrecipitation" : monthly_precip, 
        "state" : "WA", 
        "realtiveMonthlyPrecipitation" : relative_monthly_precip, 
        "station" : "GHCND :US1WAKG0038", 
        }
    }, file ) 
# 


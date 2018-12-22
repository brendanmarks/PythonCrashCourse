# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:17:50 2018

@author: Brendan
"""

import json
from pygal import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])

filepath = ("C:/Users/Brendan/Desktop/population_data.json")
with open(filepath) as f:
    pop_data = json.load(f)
    
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print (country_name +": "+ str(population))
        
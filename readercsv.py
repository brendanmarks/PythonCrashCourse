# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:49:28 2018

@author: Brendan
"""

import csv
from matplotlib import pyplot as plt

file_path = ("C:/Users/Brendan/Desktop/weatherdata.csv")
with open(file_path) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    
    highs = []
    for row in reader:
        highs.append(int(row[1]))
    print(highs)
    
    for index, column_header in enumerate(header_row):
       print(index, column_header)
       
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(highs,c='red')

plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()



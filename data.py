# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 18:51:59 2018

@author: Brendan
"""

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)
plt.scatter(2,4,s=200)
plt.plot(input_values,squares,linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major',labelsize=14)
plt.plot(squares)
plt.show()


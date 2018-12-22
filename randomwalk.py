# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:15:30 2018

@author: Brendan
"""
from random import choice 
import matplotlib.pyplot as plt

class RandomWalk():
    
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            x_dir = choice([1,-1])
            x_dist = choice([0,1,2,3,4])
            x_step = x_dir * x_dist
            
            y_dir = choice([1,-1])
            y_dist = choice([0,1,2,3,4])
            y_step = y_dir * y_dist
            
            if x_step == 0 and y_step ==0:
                continue
            
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)

while True:          
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk (y/n)?" )
    if keep_running == "n":
        break
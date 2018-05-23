# -*- coding: utf-8 -*-
"""
Created on Thu May  3 20:10:53 2018

@author: USER
"""
import random

class Planet:
    
    planetsList = []
    
    def __init__(self, name):
        self.name = name
        self.supply = {'Spice': random.randint(0, 1000),
                       'Element Zero': random.randint(0, 1000),
                       'Iron': random.randint(50, 2000),
                       'Gold': random.randint(10, 100),
                       'Helium': random.randint(200, 3000),
                       'Fuel': random.randint(10000, 15000)}
        
        self.population = random.randint(1000, 1000000)
        
        self.prices = {'Spice': round(random.uniform(1.0, 5.0), 2),
                       'Element Zero': round(random.uniform(3, 10), 2),
                       'Iron': round(random.uniform(1, 2), 2),
                       'Gold': round(random.uniform(5, 15), 2),
                       'Helium': round(random.uniform(2, 4), 2),
                       'Fuel': round(random.uniform(0.1, 2), 2)}
        
        self.economy = random.randint(10000, 20000)
        
        Planet.planetsList.append(name)
        
    def supplyReport(self, key=None):
        if key == None:
            for item in self.supply:
                print("{}: {}".format(item, self.supply[item]))
        else:
            print("{}: {}".format(key, self.supply[key]))
            
    def pricesReport(self, key=None):
        if key == None:
            for item in self.prices:
                print("{}: ${}".format(item, self.prices[item]))
        else:
            print("{}: ${}".format(key, self.supply[key]))
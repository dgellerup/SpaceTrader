# -*- coding: utf-8 -*-
"""
Created on Thu May  3 20:11:26 2018

@author: USER
"""

class Scorpion():

    def __init__(self):
        self.name = ""
        self.value = 100
        self.shipClass = "Scorpion"
        self.description = "The Scorpion is an entry-level ship, suitable for novice traders."
        self.range = 1000
        self.maxRange = 1000
        self.supply = {'Spice': 0,
                       'Element Zero': 0,
                       'Iron': 0,
                       'Gold': 0,
                       'Helium': 0}
        self.capacity = 200
        self.load = 0

    def travel(self, distance):
        if distance > self.range:
            print("That's out of range.")
        else:
            self.range = self.range - distance

    def getEncumberance(self):
        encumberance = 0

        for key in self.supply:
            encumberance += self.supply[key]

        return(encumberance)

    def renameShip(self):
        self.name = input("What would you like to name your ship? > ")

    def viewCargo(self):
        print()
        if self.name == "":
            print("You haven't named your ship. These are its stats:")
        else:
            print("Here are the stats for {}:\n".format(self.name))
        print("Value: {} credits".format(self.value))
        print("Class: {}".format(self.shipClass))
        print("Range: {} parsecs".format(self.range))
        print()
        print("Supply:")

        for key in self.supply:
            print("{}: {}".format(key, self.supply[key]))

        print()
        print("Encumberance: {}".format(self.getEncumberance()))
        print("Max Capacity: {}\n".format(self.capacity))

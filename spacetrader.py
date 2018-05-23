# -*- coding: utf-8 -*-

from planets import Planet
from ships import *


class Player:

    def __init__(self, name, age, galaxy):
        self.name = name
        self.age = age
        self.wallet = 100
        self.ship = Scorpion()
        self.location = galaxy.earth


    def viewWallet(self):
        print(self.wallet)

    def viewAge(self):
        print(self.age)

    def describeShip(self):
        print("You fly a {} valued at {} credits.".format(self.ship.shipClass, self.ship.value))

    def travel(self, distance):
        if distance > self.ship.range:
            print("That's out of range!")
        else:
            self.ship.range = self.ship.range - distance

    def buyResource(self):
        resource = input("What would you like to buy?\n")

        if resource in self.location.supply and self.location.supply[resource] > 0:
            amount = int(input("How much {} would you like to buy?\n".format(resource)))

            cost = self.location.prices[resource] * amount

            if amount <= self.location.supply[resource]:
                if resource == 'Fuel' and self.ship.range + amount <= self.ship.maxRange:

                    if cost <= self.wallet:
                        self.ship.range += amount
                        self.wallet -= cost
                        self.location.economy += cost
                        self.location.supply['Fuel'] -= amount
                    else:
                        print("You can't afford that much fuel.")

                elif resource == 'Fuel' and self.ship.range + amount > self.ship.maxRange:
                    print("That's more fuel than your ship can hold.")

                if resource != 'Fuel' and self.ship.getEncumberance() + amount <= self.ship.capacity:

                    if cost <= self.wallet:
                        self.ship.supply[resource] += amount
                        self.wallet -= cost
                        self.location.economy += cost
                        self.location.supply[resource] -= amount
                    else:
                        print("You can't afford that much {}".format(resource))
                else:
                    print("{} doesn't have that much {}".format(self.location.name, resource))
            else:
                print("{} doesn't have that much {}".format(self.location.name, resource))
        else:
            print("{} doesn't have any {} right now".format(self.location.name, resource))

    def inspectPlanetSupply(self):
        for key in self.location.supply:
            print("{}: {}".format(key, self.location.supply[key]))

    def inspectPlanetPrices(self):
        for key in self.location.prices:
            print("{}: {}".format(key, self.location.prices[key]))


class Galaxy():

    def __init__(self):
        self.earth = Planet("Earth")
        self.aarakis = Planet("Aarakis")
        self.alpha_centauri = Planet("Alpha Centauri II")
        self.coruscant = Planet("Coruscant")
        self.eden_prime = Planet("Eden Prime")
        self.titan = Planet("Titan")
        self.vulcan = Planet("Vulcan")

def printOptions():
    print("\nYou can:")
    print("1) Get Location")
    print("2) View Travel Distances")
    print("3) Travel")
    print("4) Inspect Ship")
    print("5) Rename Ship")
    print("6) View Wallet")
    print("7) Inspect Planet Supply")
    print("8) Inspect Planet Prices")
    print("9) Buy")
    print("10) Sell")
    print("11) Quit")
    print()

def main():

    galaxy = Galaxy()

    playerName = input("What is your name?\n")
    playerAge = input("How old are you?\n")

    player = Player(playerName, playerAge, galaxy)

    print()
    print("Hello {}. You start with {} credits and no cargo. You have been assigned a {}-class ship.".format(player.name, player.wallet, player.ship.shipClass))
    print()
    print("You are on {}.".format(player.location.name))

    play = True

    while play:

        topChoice = input("What would you like to do? Enter 12 for help. > ")

        try:
            if int(topChoice) == 12:
                printOptions()

            if int(topChoice) == 11:
                play = False

            elif int(topChoice) == 1:
                print(player.location.name)
                print()

            elif int(topChoice) == 2:

                print()

            elif int(topChoice) == 3:

                print()

            elif int(topChoice) == 4:
                player.ship.viewCargo()
                print()

            elif int(topChoice) == 5:
                player.ship.renameShip()
                print("{} is a fitting name.".format(player.ship.name))
                print()

            elif int(topChoice) == 6:
                player.viewWallet()
                print()

            elif int(topChoice) == 7:
                player.inspectPlanetSupply()
                print()

            elif int(topChoice) == 8:
                player.inspectPlanetPrices()
                print()

            elif int(topChoice) == 9:

                print()

            elif int(topChoice) == 10:

                print()

            else:
                print("Please enter an integer corresponding to an action.")

        except ValueError:
            print("Please enter an integer corresponding to an action.\n")




if __name__ == "__main__":
    main()

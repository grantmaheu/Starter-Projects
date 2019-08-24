### Simulates the roll of a dice ###

import random

def dieRoll(n): #Rolls the dice
    range = int(input("How many sides does the dice have? "))
    roll = random.randint(1, range)
    print("The die rolled a %d" %roll)

roll()

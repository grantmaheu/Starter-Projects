### File simulates the roll of a dice ###

import random

#range = int(input("How many sides to the dice? "))
range = 6
i = 0
it = 10000

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

def dieRoll(n): #Rolls the dice
    roll = random.randint(1, n+1)
    return roll
    #print("The die rolled a %d" %roll)

while i <= it: #Determines the frequentest probability
    x = dieRoll(range)
    if x == 1:
        count1 += 1
    elif x == 2:
        count2 += 2
    elif x == 3:
        count3 += 3
    elif x == 4:
        count4 += 4
    elif x == 5:
        count5 += 5
    else:
        count6 += 6
    i += 1

sum = count1+count2+count3+count4+count5+count6
print(sum)

"""
print("the probability of the die being a 1 is: ",100*count1/it,"%")
print("the probability of the die being a 2 is: ",100*count2/it,"%")
print("the probability of the die being a 3 is: ",100*count3/it,"%")
print("the probability of the die being a 4 is: ",100*count4/it,"%")
print("the probability of the die being a 5 is: ",100*count5/it,"%")
print("the probability of the die being a 6 is: ",100*count6/it,"%")
"""
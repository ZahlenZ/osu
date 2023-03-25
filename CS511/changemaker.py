import sys
import time

number = int(sys.argv[1])        # store the "number"
factors = [int(sys.argv[n + 2]) for n in range(len(sys.argv[:]) - 2)]     # create the "coins" array
factors.insert(0, 1)     # assume we always have a "unit" coin

def changemaker(number, factors): 
    place = [float("inf") for itr in range(number + 1)]     # array to store the solutions
    place[0] = 0 
    for factor in factors:
        for i in range(len(place)):
            if factor <= i:
                place[i] = min(place[i], 1 + place[i - factor])     # is previous solution, if add 1 to that many coins
    return place[number]    # always have a "unit" coin, shouldn't return "inf"

print(changemaker(number, factors))
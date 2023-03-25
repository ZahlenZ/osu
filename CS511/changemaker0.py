# %%
import sys
import time

#%%
number = int(sys.argv[1])        # store the "number"
factors = [int(sys.argv[n + 2]) for n in range(len(sys.argv[:]) - 2)]     # create the "coins" array
factors.insert(0, 1)     # assume we always have a "unit" coin

# Define changemaker
#%%
def changemaker(number, factors): 
    place = [float("inf") for itr in range(number + 1)]     # array to store the solutions
    place[0] = 0 
    for factor in factors:
        for i in range(len(place)):
            if factor <= i:
                place[i] = min(place[i], 1 + place[i - factor])     # is previous solution, if add 1 to that many coins
    return place[number]    # always have a "unit" coin, shouldn't return "inf"

# Test changemaker
#%%
my_coins = [3, 5, 7]   # fibonacci land
denom_test1 = [10, 20, 40, 60]
tt_dynamic = list()

for denom in denom_test1:
    start = time.process_time()
    changemaker(denom, my_coins)
    end = time.process_time()
    tt_dynamic.append(end - start)

# Define num_coins
#%%
def num_coins(amount, coins, count):
    if 1 not in coins:
        print("A penny for your thoughts on why you thought this would work with a penny?")
        return
    min_coins = None
    if amount == 0:
        return count
    for c in coins:
        if c <= amount:
            cur_count = num_coins(amount-c, coins, count+1)
            if min_coins is None or cur_count < min_coins:
                min_coins = cur_count
    return min_coins

# Test num_coins
#%% 
my_coins = [1, 5, 10, 25, 50]   # need to live in normal land so this wont take forever
denom_test = [10, 20, 40, 60]
tt_recursive = list()

for denom  in denom_test:
    start = time.process_time()
    num_coins(amount = denom, coins = my_coins, count = 0)
    end = time.process_time()
    tt_recursive.append(end - start)

#%%
import matplotlib.pyplot as plt

plt.plot(denom_test1, tt_dynamic, label = "Dynamic Change")
plt.plot(denom_test, tt_recursive, label = "Recursive Change")
plt.legend(loc = "best")
# %%

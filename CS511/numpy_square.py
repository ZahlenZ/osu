import numpy as np
import sys

file = open(sys.argv[1])
int_list = file.read()
file.close()

int_list = np.genfromtxt("array-final-2d.txt", delimiter = ",",
                        dtype = int).reshape(50, 50) # Turn the single line of integers into 50X50
blocks = np.lib.stride_tricks.as_strided(int_list,      
                                        shape = (48, 48, 3, 3), # 48 X 48 array of 3 X 3
                                        strides = int_list.strides + int_list.strides) # Same column next row twice

all_sums = dict() # sums & count of occurrances
max_sum = dict() # max sums and locations
is_max = 0

for i in range(len(blocks)): 
    for j in range(len(blocks)): # For all of the block
        next_sum = np.sum(blocks[i, j]) # Sum the current block

        if str(next_sum) not in all_sums.keys(): # Do we know of this sum yet
            all_sums[str(next_sum)] = 1 # New sum storage
        else:
            all_sums[str(next_sum)] += 1 # Known sum occurrance count

        if next_sum >= is_max:
            max_sum[str(i) + "," + str(j)] = next_sum # max sum storage key = coordinate 
            is_max = next_sum # Set "local max"

abs_max = max(list(max_sum.values())) # Find "global max"
print("The Maximum sum is: " +
        str(max(list(max_sum.values()))) +
        ". " +
        "The location is: " +
        str(list(max_sum.keys())[list(max_sum.values()).index(abs_max)]))

max_occurrance = max(list(all_sums.values())) # Max occurances
common_sums = list() # List to store values that occure the same as max_occurrances

for sum in list(all_sums.keys()): 
    if all_sums[sum] == max_occurrance:
        common_sums.append(sum)
    else:
        pass

print("The most common sum(s) are: " +
        str(common_sums) +
        "\nThey occur: " +
        str(max_occurrance))


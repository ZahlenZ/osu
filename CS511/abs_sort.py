# %%
def abs_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    for i in range(len(sorted_list)):
        sorted = True
        for j in range(len(sorted_list) - 1):
            if abs(sorted_list[j]) > abs(sorted_list[j + 1]):
                move_number = sorted_list.pop(j)
                sorted_list.insert(j + 1, move_number)
                sorted = False
            elif abs(sorted_list[j]) == abs(sorted_list[j + 1]) and sorted_list[j] < 1:
                move_number = sorted_list.pop(j)
                sorted_list.insert(j + 1, move_number)
                sorted = False
        if sorted:
            break
    return sorted_list


def abs_sort_in_place(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list) - 1):
            if abs(unsorted_list[j]) > abs(unsorted_list[j + 1]):
                move_number = unsorted_list.pop(j)
                unsorted_list.insert(j + 1, move_number)
            elif abs(unsorted_list[j]) == abs(unsorted_list[j + 1]) and unsorted_list[j] < 1:
                move_number = unsorted_list.pop(j)
                unsorted_list.insert(j + 1, move_number)

# %%

import random
import time

sort_me = [random.randint(-100, 100) for iter in range(5000)]

# %%
start = time.process_time()
abs_sort(sort_me)
end = time.process_time()
print("It took: " + str(end - start))

# %%
def merge(l, r):
    i = 0
    j = 0
    result = []
    while (len(result) < len(r)+len(l)):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
        if i == len(l) or j == len(r):  # if we are at the end of one of the lists
            result.extend(l[i:] or r[j:])  # appends the remainder of the list that has elements left
            break
    return result

def mergesort(arr):
    subarray_size = 1  # The size of our subarrays we will be merging
    left_index = 0  # The start of the left subarray
    # While a sub array is still smaller than our array to sort
    while subarray_size < len(arr):
    # While there is still enough room to have a left and right subarray
        while  left_index+subarray_size < len(arr):
            right_index = left_index + subarray_size  # The start of the right subarray
            next_subarray = min(left_index + subarray_size*2, len(arr))  # The index to the right of the   last index of the right subarray
        # Replace a slice of the array with the two merged halves of that slice
            arr[left_index:next_subarray] = merge(arr[left_index:left_index+subarray_size],       
                                                        arr[right_index:next_subarray])
        # Move   down the array to the next subarray not hit in this pass
            left_index = next_subarray
    # Double the sub array slice size
    subarray_size = subarray_size * 2
    left_index = 0
    return arr

# lets try and set up a sort function here that follows the ideas presented on recurssion and appending.

# %%
def sort_faster(array):
    if len(array) < 2:
        return array
    
    less_than, same, greater_than = [], [], []

    pivot = array[random.randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            less_than.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            greater_than.append(item)
    
    return sort_faster(less_than) + same + sort_faster(greater_than)

# %%
array = [random.randint(-1000000, 1000000) for iter in range(160000)]

start = time.process_time()
sort_faster(array)
end = time.process_time()
print("It took: " + str(end - start))

# %%

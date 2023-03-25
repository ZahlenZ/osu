# This is my original function
def abs_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list) - 1):
            if abs(sorted_list[j]) > abs(sorted_list[j + 1]):
                move_number = sorted_list.pop(j)
                sorted_list.insert(j + 1, move_number)
            elif abs(sorted_list[j]) == abs(sorted_list[j + 1]) and sorted_list[j] < 1:
                move_number = sorted_list.pop(j)
                sorted_list.insert(j + 1, move_number)
        if sorted:
            break
    return sorted_list

# This is the my attempt to improve the time
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


import random
import time

# Timing the orginal and updated original function (all done in notebooks which is why they have the same name)
sort_me = [random.randint(-100, 100) for iter in range(5000)]
start = time.process_time()
abs_sort(sort_me)
end = time.process_time()
print("It took: " + str(end - start))

# Concept and function I found online as I couldn't wrap my head around improved sort time this week
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

array = [random.randint(-1000000, 1000000) for iter in range(160000)]

# Timing the new function
start = time.process_time()
sort_faster(array)
end = time.process_time()
print("It took: " + str(end - start))
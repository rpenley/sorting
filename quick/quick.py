#!/usr/bin/python
# Using python 3.9

import random

# performance tracking variables
swaps = 0
comparisons = 0

# Generate random array to sort
def genNumbers(size, scale):
	array = [random.randint(0,scale) for x in range(size)]
	return array

def partition(array, start, end):
	global swaps
	global comparisons
	i = (start - 1)
	pivot = array[end]	
	for j in range(start, end):
		comparisons += 1
		if array[j] <= pivot:
			i += 1
			swaps += 1
			array[i], array[j] = array[j], array[i]
	swaps += 1
	array[i+1], array[end] = array[end], array[i+1]
	return (i+1)

def quickSort(array, start, end):
	global swaps
	global comparisons
	if len(array) == 1:
		return array
	comparisons += 1
	if start < end:
		parted = partition(array, start, end)
		quickSort(array, start, parted - 1)
		quickSort(array, parted + 1, end)

array = genNumbers(20, 50)
print("Unsorted: " + str(array))
quickSort(array, 0, len(array) - 1)
print("Sorted: " + str(array))
print("number of items: " + str(len(array)))
print("comparisons: " + str(comparisons))
print("swaps: " + str(comparisons))

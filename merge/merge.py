#!/usr/bin/python
# Using python 3.9

import random

# performance tracking variables
copies = 0
comparisons = 0

# Generate random array to sort
def genNumbers(size, scale):
	array = [random.randint(0,scale) for x in range(size)]
	return array

def merge(array, left, mid, right):
	global copies
	global comparisons
	leftSize = mid - left + 1 
	rightSize = right - mid
	leftArr = [0] * (leftSize)
	rightArr = [0] * (rightSize)
	copies += 2
	for i in range(0, leftSize):
		leftArr[i] = array[left + i]
	for j in range(0, rightSize):
		rightArr[j] = array[mid + 1 + j]	

	i = 0
	j = 0
	k = left

	while i < leftSize and j < rightSize:
		comparisons += 1
		if leftArr[i] <= rightArr[j]:	
			array[k] = leftArr[i]
			i += 1
		else:
			array[k] = rightArr[j]
			j += 1
		k += 1

	comparisons += 1
	while i < leftSize:
		array[k] = leftArr[i]
		i += 1
		k += 1
	
	comparisons += 1
	while j < rightSize:
		array[k] = rightArr[j]
		j += 1
		k += 1

def mergesort(array, left, right):
	if left < right:
		mid = (left + (right - 1)) // 2
		leftArray = mergesort(array, left, mid)
		rightArray = mergesort(array, mid + 1, right)
		merge(array, left, mid, right)

array = genNumbers(20, 50)
print("Unsorted: " + str(array))
mergesort(array, 0, len(array) - 1)
print("Sorted: " + str(array))
print("number of items: " + str(len(array)))
print("comparisons: " + str(comparisons))
print("copies: " + str(copies))

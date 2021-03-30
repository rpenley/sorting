#!/usr/bin/python
# Using python 3.9

import random

# Generate random numbers to sort
def genNumbers(size):
	numbers = [random.randint(0,9) for x in range(size)]
	return numbers

def bubbleSort(numbers):
	n = len(numbers)	
	count = 0
	for i in range(n):
		for j in range(n-i-1):
			#print(numbers)
			if numbers[j] > numbers[j+1]:
				count = count + 1
				numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
	print("sort took " + str(count) + " operations to complete")
	return numbers
unsortedNumbers = genNumbers(20)
print("Unsorted: " + str(unsortedNumbers))
sortedNumbers = bubbleSort(unsortedNumbers)
print("Sorted: " + str(sortedNumbers))

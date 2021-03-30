#!/usr/bin/python
# Using python 3.9

import random

# Generate random numbers to sort
def genNumbers(size):
	numbers = [random.randint(0,9) for x in range(size)]
	return numbers

def bogoSort(numbers):
	count = 0
	randNumbers = genNumbers(len(numbers))
	while (randNumbers != numbers):
		count = count + 1
		randNumbers = genNumbers(len(numbers))
	print("BOGO! in " + str(count) + " generations")

numbers = genNumbers(5)
bogoSort(numbers)

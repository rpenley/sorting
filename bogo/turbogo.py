#!/usr/bin/python
# Using python 3.9

import random
import threading
import os
import signal

# Generate random numbers to sort
def genNumbers(size):
	numbers = [random.randint(0,9) for x in range(size)]
	return numbers

def bogoSort(numbers, count):
	randNumbers = genNumbers(len(numbers))
	while (randNumbers != numbers):
		randNumbers = genNumbers(len(numbers))
		count = count + 1
	print("BOGO in " + str(count) + " operations")
	os._exit(0)

numbers = genNumbers(7)
count = 0
t0 = threading.Thread(target=bogoSort, args=(numbers,count,))
t1 = threading.Thread(target=bogoSort, args=(numbers,count,))
t2 = threading.Thread(target=bogoSort, args=(numbers,count,))
t3 = threading.Thread(target=bogoSort, args=(numbers,count,))
t4 = threading.Thread(target=bogoSort, args=(numbers,count,))
t5 = threading.Thread(target=bogoSort, args=(numbers,count,))
t6 = threading.Thread(target=bogoSort, args=(numbers,count,))
t7 = threading.Thread(target=bogoSort, args=(numbers,count,))
t8 = threading.Thread(target=bogoSort, args=(numbers,count,))
t9 = threading.Thread(target=bogoSort, args=(numbers,count,))

t0.start()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()

t0.join()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()


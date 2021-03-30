#!/usr/bin/python
import matplotlib.pyplot as plt 
import random

# Generate random numbers to sort
def genNumbers(size, numRange):
	numbers = [random.randint(0,numRange) for x in range(size)]
	return numbers

def bubbleSort(left, height):
	n = len(height)	
	plt.xlabel('x - axis') 
	plt.ylabel('y - axis') 
	plt.title('Sort') 
	fig = plt.figure()
	barGraph = plt.bar(left, height,	width = 1, color = ['red', 'green']) 
	plt.show()
	swaps = 0
	comparisons = 0
	for i in range(n):
		for j in range(n-i-1):
			comparisons = comparisons + 1
			if height[j] > height[j+1]:
				swaps = swaps + 1
				height[j], height[j+1] = height[j+1], height[j]
				fig.clear()
				barGraph = plt.bar(left, height,	width = 1, color = ['red', 'green'])
				fig.canvas.draw()
#print("sort took " + str(comparisons) + " operations to complete")

# x-coordinates of left sides of bars  
left = []
for i in range(100):
	left.append(i)
	 
def updateGraph(left,height):
	plt.show()
	  
# heights of bars 
height = genNumbers(100,100)
	  
# labels for bars 
#tick_label = ['one', 'two', 'three', 'four', 'five'] 
  
# plotting a bar chart 
#plt.bar(left, height, tick_label = tick_label,	width = 0.8, color = ['red', 'green']) 
#plt.bar(left, height,	width = 1, color = ['red', 'green']) 
  
# naming the x-axis 
# naming the y-axis 
# plot title 
  
# function to show the plot 
#plt.show() 

#unsortedNumbers = genNumbers(20)
#print("Unsorted: " + str(height))
sortedNumbers = bubbleSort(left, height)
#print("Sorted: " + str(sortedNumbers))

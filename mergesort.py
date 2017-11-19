# Mergesort algorithm in Python

import sys

# function to be called on a list
def mergesort(unsortedList):
	mergesortIndex(unsortedList, 0, len(A)-1)

def mergesortIndex(unsortedList, first, last):
	if first < last:
		middle = (first + last)//2
		mergesortIndex(unsortedList, first, middle)
		mergesortIndex(unsortedList, middle+1, last)
		merge(unsortedList, first, middle, last)

def merge(unsortedList, first, middle, last):
	left = unsortedList[first:middle+1]
	right = unsortedList[middle+1:last+1]
	left.append(sys.maxsize)
	right.append(sys.maxsize)
	i = j = 0

	for k in range(first, last+1):
		if left[i] <= right[j]:
			unsortedList[k] = left[i]
			i += 1
		else:
			unsortedList[k] = right[j]
			j += 1

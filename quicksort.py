# Quicksort algorithm in Python

def quicksort(unsortedList):
	quicksortIndex(unsortedList0, len(unsortedList)-1)

def quicksortIndex(unsortedListlowerIndex, higherIndex):
	if higherIndex-lowerIndex < threshold and lowerIndex < higherIndex:
		quickSelection(unsortedListlowerIndex, higherIndex)
	elif lowerIndex < higherIndex:
		p = partition(unsortedListlowerIndex, higherIndex)
		quicksortIndex(unsortedListlowerIndex, p - 1)
		quicksortIndex(unsortedListp + 1, higherIndex)

def getPivot(unsortedListlowerIndex, higherIndex):
	midIndex = (higherIndex + lowerIndex) // 2
	s = sorted([unsortedList[lowerIndex], unsortedList[midIndex], unsortedList[higherIndex]])
	if s[1] == unsortedList[lowerIndex]:
		return lowerIndex
	elif s[1] == unsortedList[midIndex]:
		return midIndex
	return higherIndex

def partition(unsortedListlowerIndex, higherIndex):
	pivotIndex = getPivot(unsortedListlowerIndex, higherIndex)
	pivotValue = unsortedList[pivotIndex]
	unsortedList[pivotIndex], unsortedList[lowerIndex] = unsortedList[lowerIndex], unsortedList[pivotIndex]
	border = lowerIndex

	for i in range(lowerIndex, higherIndex+1):
		if unsortedList[i] < pivotValue:
			border += 1
			unsortedList[i], unsortedList[border] = unsortedList[border], unsortedList[i]
	unsortedList[lowerIndex], unsortedList[border] = unsortedList[border], unsortedList[lowerIndex]

	return (border)

def quickSelection(x, first, last):
	for i in range (first, last):
		minIndex = i
		for j in range (i+1, last+1):
			if x[j] < x[minIndex]:
				minIndex = j
		if minIndex != i:
			x[i], x[minIndex] = x[minIndex], x[i]

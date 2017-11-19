# Bubblesort algorithm in Python

def bubblesort(unsortedList):
	for i in range (0, len(unsortedList) - 1):
		isSorted = True
		for j in range (0, len(unsortedList) - i - 1):
			if unsortedList[j] > unsortedList[j+1]:
				unsortedList[j], unsortedList[j+1] = unsortedList[j+1], unsortedList[j]
				isSorted = False
		if isSorted:
			return unsortedList

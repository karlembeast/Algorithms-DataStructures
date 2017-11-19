# Insertionsort algorithm in Python

def insertionsort(unsortedList):
	for i in range(1, len(unsortedList)):
		currentNumber = unsortedList[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if unsortedList[j] > currentNumber:
				unsortedList[j+1] = unsortedList[j]
			else:
				break
		unsortedList[k+1] = currentNumber

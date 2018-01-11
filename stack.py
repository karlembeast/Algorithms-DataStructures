class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.top = None

	def push(self, item):
		node = Node(item)
		if self.top is None:
			self.top = node
		else:
			node.next = self.top
			self.top = node

	def pop(self):
        if self.top is None:
			return None
		else:
			temp = self.top.data
			oth = self.top.next
			self.top.next = None
			self.top = oth
			return temp

	def getTop(self):
		return self.top.data

	def printStack(self):
		currentNode = self.top
		while currentNode is not None:
			print(currentNode.data)
			currentNode = currentNode.next

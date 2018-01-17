# Queue implemented with two stacks

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
            raise NameError("nothing to pop out from")
        else:
            temp = self.top.data
            oth = self.top.next
            self.top.next = None
            self.top = oth
            return temp

    def size(self):
        newNode = Node()
        c = 0
        newNode.top = self.top
        while(newNode.top != None):
            newNode.pop()
            c=c+1
        return c

	def getTop(self):
		return self.top.data

	def printStack(self):
		currentNode = self.top
		while currentNode is not None:
			print(currentNode.data)
			currentNode = currentNode.next

    def isEmpty(self):
        return self.top == None

class myQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,item):
        self.stack1.push(item)

    def dequeue(self):
        if not self.stack1.isEmpty():
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())
            res = self.stack2.pop()
            while self.stack2.size() > 0:
                self.stack1.push(self.stack2.pop())

q = myQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
a = q.dequeue()
print(a)
b = q.dequeue()
print(b)
c = q.dequeue()
print(c)
d = q.dequeue()
print(d)
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())

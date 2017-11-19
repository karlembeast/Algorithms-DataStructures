# DoublyLinkedList Data Structure in Python

class Node(object):

    def __init__ (self, d, n = None, p = None):
        self.data = d
        self.nextNode = n
        self.prevNode = p

    def getNext (self):
        return self.nextNode

    def setNext (self, n):
        self.nextNode = n

    def getPrev (self):
        return self.prevNode

    def setPrev (self, p):
        self.prevNode = p

    def getData (self):
        return self.data

    def setData (self, d):
        self.data = d


class LinkedList (object):

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def getSize (self):
        return self.size

    def add (self, d):
        newNode = Node (d, self.root)
        if self.root:
            self.root.setPrev(newNode)
        self.root = newNode
        self.size += 1

    def remove (self, d):
        thisNode = self.root

        while thisNode:
            if thisNode.getData() == d:
                next = thisNode.getNext()
                prev = thisNode.getPrev()

                if next:
                    next.setPrev(prev)
                if prev:
                    prev.setNext(next)
                else:
                    self.root = thisNode
                self.size -= 1
                # data removed
                return True
            else:
                thisNode = thisNode.getNext()
        # data not found
        return False

    def find (self, d):
        thisNode = self.root
        while thisNode:
            if thisNode.getData() == d:
                return d
            else:
                thisNode = thisNode.getNext()
        return None

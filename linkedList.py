# LinkedList Data Structure in Python

class Node(object):
    def __init__ (self, d, n = None):
        self.data = d
        self.nextNode = n

    def getNext (self):
        return self.nextNode

    def set_next (self, n):
        self.nextNode = n

    def getData (self):
        return self.data

    def set_data (self, d):
        self.data = d


class LinkedList (object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def getSize (self):
        return self.size

    def add (self, d):
        newNode = Node (d, self.root)
        self.root = newNode
        self.size += 1

    def remove (self, d):
        thisNode = self.root
        prevNode = None

        while thisNode:
            if thisNode.getData() == d:
                if prevNode:
                    prevNode.setNext(thisNode.getNext())
                else:
                    self.root = thisNode.getNext()
                self.size -= 1
                # data removed
                return True
            else:
                prevNode = thisNode
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

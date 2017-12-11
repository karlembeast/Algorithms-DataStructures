# Binary Search Tree Data Structure in Python

class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            return False

        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if (self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def getHeight(self):
        if self.leftChild and self.rightChild:
            return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
        elif self.leftChild:
            return 1 + self.leftChild.getHeight()
        elif self.rightChild:
            return 1 + self.rightChild.getHeight()
        else:
            return 1

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return -1

    def remove(self, data):
        # check if the tree is empty
        if self.root is None:
            return False

        # data is in root node
        elif self.root.value == data:
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.root.rightChild
            elif self.root.leftChild and self.root.rightChild:
                deleteNodeParent = self.root
                deleteNode = self.root.rightChild
                while deleteNode.leftChild:
                    deleteNodeParent = deleteNode
                    deleteNode = deleteNode.leftChild

                self.root.value = deleteNode.value
                if deleteNode.rightChild:
                    if deleteNodeParent.value > deleteNode.value:
                        deleteNodeParent.leftChild = deleteNode.rightChild
                    elif deleteNodeParent.value < deleteNode.value:
                        deleteNodeParent.rightChild = deleteNode.rightChild
                else:
                    if deleteNode.value < deleteNodeParent.value:
                        deleteNodeParent.leftChild = None
                    else:
                        deleteNodeParent.rightChild = None

            return True

        parent = None
        node = self.root

        # search for the node to be removed
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.leftChild
            elif data > node.value:
                node = node.rightChild

        # case 1: node not in the BST
        if node is None or node.value != data:
            return False

        # case 2: the node to be removed has no children
        elif node.leftChild is None and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return True

        # case 3: the node to be removed has left child only
        elif node.leftChild and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
            return True

        # case 4: the node to be removed has right child only
        elif node.leftChild is None and node.rightChild:
            if data < parent.value:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return True

        # case 5: the node to be removed has both left and right children
        else:
            deleteNodeParent = node
            deleteNode = node.rightChild
            while deleteNode.leftChild:
                deleteNodeParent = deleteNode
                deleteNode = deleteNode.leftChild
            node.value = deleteNode.value
            if deleteNode.rightChild:
                if deleteNodeParent.value > deleteNode.value:
                    deleteNodeParent.leftChild = deleteNode.rightChild
                elif deleteNodeParent.value < deleteNode.value:
                    deleteNodeParent.rightChild = deleteNode.rightChild
            else:
                if deleteNode.value < deleteNodeParent.value:
                    deleteNodeParent.leftChild = None
                else:
                    deleteNodeParent.rightChild = None

    def preorder(self):
        if self.root is not None:
            print("PreOrder of BST: ")
            self.root.preorder()

    def postorder(self):
        if self.root is not None:
            print("PostOrder of BST: ")
            self.root.postorder()

    def inorder(self):
        if self.root is not None:
            print("InOrder of BST: ")
            self.root.inorder()


#This is the code for the implementation of a binary search tree data structure
#using python 3.9.1 @CharlesNorris 
#the 26/03/21 

class Node:

    def __init__(self):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, self.root)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, node):
        #We have to visit the left sub tree 
        if data < Node.data:
            if Node.leftChild:
                insert_node(data, node.leftChild)
            else:
                Node.leftChild = Node(data, node)
            #We have to visit the right subTree
        else:
            if Node.rightChild:
                self.insert_node(data, Node.rightChild)
            else:
                Node.rightChild = Node(data, node)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if Node.rightChild:
            return get_max(Node.rightChild)
        return Node.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if Node.leftChild:
            return get_min(Node.leftChild)
        return Node.data

    def traverse_in_order(self, node):
        if Node.leftChild:
            self.traverse_in_order(Node.leftChild)
        print('%s' % Node.data)

        if Node.rightChild:
            self.traverse_in_order(Node.rightChild)
 

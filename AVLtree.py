#This is the implementation of a AVL Tree abstract data structure
#Using python 3.9.1 by @CharlesNorris


class Node:

    def __init__(self, data, parent):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0

class AVLtree:

    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data :
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data, node)
                node.height = max(self.calc_height(node.height), self.calc_height(node.right_node)) + 1
        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data, node)
                node.height = max(self.calc_height(node.height), self.calc_height(node.left_node)) + 1

        self.handle_violation(parent)

    def remove_node(self, data, node):
        if node is none:
            return
        
        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            if node.left_node is None and node.right_node is None:
                print("Removing leaf node ,", node.data)
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                elif parent is not None and parent.right_node == node:
                    parent.right_node = None

                if parent is None:
                    self.root = None

                del node

                self.handle_violation(parent)

            elif node.left_node is None and node.right_node is not None:
                print("Removing a node with a single right child...")
                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.right_node
                else:
                    self.root = node.right_node

                node.right_node.parent = parent
                del node

            elif node.right_node is None and node.left_node is not None:
                print("Removing a node with a single left child")
                parent = node.parent

                
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node

                self.handle_violation(parent)
            else:
                print("Removing a node with two children")

                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)

        return node

    def handle_violation(self, node):
        while node is not none:
            node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
            self.violation_helper(node)
            node = node.parent


    def violation_helper(self, node):
        balance = self.calculate_balance(node)

        if balance > 1:
            if self.calculate_balance(node.left_node) < 0:
                self.rotate_left(node.left_node)

            self.rotate_right(node)

        if balance < -1:
            if self.calculate_balance(node.right_node) > 0:
                self.rotate_right(node.right_node)

            self.rotate_left(node)

    def calc_height(self, node):

        if node is None:
            return -1

        return node.height

    def calculate_balance(self, node):

        if node is None:
            return 0

        return self.calc_height(node.left_node) - self.calc_height(node.right_node)

    def rotate_right(self, node):
        print("Rotating to the right on node", node.data)

        temp_left_node = node.left_node
        T = temp_left_node.right_node

        temp_left_node.right_child = node
        node.left_node - T

        if T is not None:
            T.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node
        
        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
        temp_left_node.height = max(self.calc_height(temp_left_node.left_node), self.calc_height(temp_left_node.right_node)) + 1


    def rotate_left(self, node):
        print("Rotating to the left on node", node.data)

        temp_right_node = node.right_node
        T = temp_right_node.left_node

        temp_right_node.left_child = node
        node.right_node - T

        if T is not None:
            T.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.left_node = temp_right_node
        
        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node

        node.height = max(self.calc_height(node.right_node), self.calc_height(node.left_node)) + 1
        temp_right_node.height = max(self.calc_height(temp_right_node.right_node), self.calc_height(temp_right_node.left_node)) + 1


avl = AVLtree()










class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root

        while True:
            if temp.value == new_node.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                   temp.left = new_node
                   return True
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.rigth

    def contain(self, value):
        if self.root is None:
            return False
        
        temp = self.root

        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
            
        return False

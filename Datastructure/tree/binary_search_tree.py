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
    # O(logn)
    def contain(self, value):
        temp = self.root

        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
            
        return False

    # RECURSIVE way to find a contain
    # O(logn)
    def __r_contains(self, current, value):
        if current == None:
            return False
            
        if current.value == value:
            return True
            
        if value < current.value:
            return self.__r_contains(current.left, value)
        
        if value >  current.value:
            return self.__r_contains(current.right, value)
            
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    # O(logn)
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
            
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
            
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    # O(logn)
    def __delete_node(self, current_node, value):
        # value is not in the tree
        if current_node == None:
            return None
            
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
            
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
            
        # value == current_node.value
        else:
            # current node is leaf node
            if current_node.left == None and current_node.right == None:
                current_node = None
            # has left no right
            elif current_node.right == None:
                current_node = current_node.left
            # has right no left
            elif current_node.left == None:
                current_node = current_node.right
            # has both
            else:
                min_value = self.min_value(current_node.right)
                current_node.value = min_value
                current_node.right = self.__delete_node(current_node.right, min_value)
        return current_node
        
    def delete_node(self, value):
        self.__delete_node(self.root, value)

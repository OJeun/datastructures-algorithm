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


    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst(self, nums, left, right):
        if left == right:
            new_node = Node(nums[left])
            return new_node
            
        if left > right:
            return None
            
        mid = (left + right) // 2
        mid_node = Node(nums[mid])
        
        left_sub_tree = self.__sorted_list_to_bst(nums, left, mid-1)
        right_sub_tree = self.__sorted_list_to_bst(nums, mid + 1, right)
        
        mid_node.left = left_sub_tree
        mid_node.right = right_sub_tree
        
        return mid_node

    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, node):
        if node is None:
            return None
            
        left_sub_tree = self.__invert_tree(node.left)
        right_sub_tree = self.__invert_tree(node.right)
        
        node.left = right_sub_tree
        node.right = left_sub_tree
        
        return node
    
    # O(n)
    def BFS(self):
        current = self.root
        queue = []
        results = []
        queue.append(current)
        
        while len(queue) > 0:
            current = queue.pop(0)
            results.append(current.value)
            
            # append left and right nodes of current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return results
    
    # O(n)
    def dfs_pre_order(self):
        current_node = self.root
        results = []
        
        def traverse(current):
            results.append(current.value)
            
            if current.left:
                traverse(current.left)
                
            if current.right:
                traverse(current.right)
                
        traverse(current_node)
        return results
    
    def kth_smallest(self, k):
        self.kth_smallest_count = 0
        return self.kth_smallest_helper(self.root, k)
 
    def kth_smallest_helper(self, node, k):
        if node is None:
            return None
 
        left_result = self.kth_smallest_helper(node.left, k)
        if left_result is not None:
            return left_result
 
        self.kth_smallest_count += 1
        if self.kth_smallest_count == k:
            return node.value
 
        right_result = self.kth_smallest_helper(node.right, k)
        if right_result is not None:
            return right_result
 
        return None
    
    def kth_smallest_with_stack(self, k):
        current_node = self.root
        stack = []
        
        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
                
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.value
                
            
            current_node = node.right
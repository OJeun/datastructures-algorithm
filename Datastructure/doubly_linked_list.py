class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp:
            print(temp.valje)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            temp = self.tail
            temp.next = new_node
            new_node.prev = temp
            new_node.next = None
            self.tail = new_node
        
        self.length += 1
        return True
    
    # O(1)
    def pop(self):
        if self.head is None:
            return None
        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        
        self.length -= 1
        return temp
        
    def prepend(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        
        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        
        self.length -= 1
        return temp
    
    def get(self, index):
        half = self.length // 2
        temp = None

        if index < 0 or index >= self.length:
            return None

        if index < half:
            temp = self.head
            for i in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length - index - 1):
                temp = temp.prev
        
        return temp
    
    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        else:
            return False
        
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        after = self.get(index)
        prev = after.prev

        new_node.next = after
        new_node.prev = after.prev

        prev.next = new_node
        after.prev = new_node
        return True
    
    def remove(self, index):
        to_be_removed = self.get(index)
        
        if to_be_removed is None:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        prev = to_be_removed.prev
        next = to_be_removed.next

        prev.next = next
        next.prev = prev
        self.length -= 1

        to_be_removed.next = None
        to_be_removed.prev = None

        return to_be_removed
    
    def reverse(self):
        temp = self.head
        
        while temp:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev
        
        self.head, self.tail = self.tail, self.head 
    
    def swap_first_last(self):
        if self.length == 0:
            return False
        value = self.head.value
        self.head.value = self.tail.value
        self.tail.value = value
        return True
    
    def is_palindrome(self):
        start = self.head
        end = self.tail
        
        for i in range(self.length // 2):
            if start.value != end.value:
                return False
            start = start.next
            end = end.prev
            
        return True
    
    def swap_pairs(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node

        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next

            # keep dummy to be connected to the head
            previous_node.next = second_node

            # Swap a pair of nodes
            first_node.next = second_node.next
            second_node.next = first_node
            first_node.prev = second_node
            second_node.prev = previous_node

            # Move the pointer
            previous_node = first_node
            self.head = first_node.next

        self.head = dummy_node.next
        self.head.prev = None



        





    
        


            

            


        
        

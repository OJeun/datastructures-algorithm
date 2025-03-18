class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp.next is not None:
            print(temp.value)
            temp = temp.next

    # O(1)
    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    # O(n)
    def pop(self):
        if self.head and self.tail:
            first_pointer = self.head
            second_pointer = self.head
            while first_pointer.next:
                second_pointer = first_pointer
                first_pointer = first_pointer.next
            self.tail = second_pointer
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return first_pointer
        else:
            return None
    # O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    # O(1)
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp

    # O(n)
    def get(self, index):
        if index >= self.length + 1 or index < 0:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    # O(n)
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False
            
    # O(n)
    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        pre = self.get(index - 1)
        new_node.next = pre.next
        pre.next = new_node
        self.length += 1
        return True
    
    # O(n)
    def remove(self, index):
        if index > self.length - 1 or index < 0:
            return None
        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.pop_first()
        pre = self.get(index -1)
        temp = pre.next
        pre.next = temp.next
        return temp

    # O(n)
    def reverse(self):
        # Swap head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        current = temp
        

        for _ in range(self.length):
            after = current.next
            current.next = before
            before = current
            current = after





        
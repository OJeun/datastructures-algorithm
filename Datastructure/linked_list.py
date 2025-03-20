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

    # O(n), why it should use three pointers?
    def reverse(self):
        before = None
        current = self.head
        after = current.next

        temp = self.head
        self.head = self.tail
        self.tail = temp

        while current:
            current.next = before
            before = current
            current = after
            after = after.next



    # O(n), careful with the condition on while loop
    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    # O(n)
    def has_loop(self):
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
    # O(1)
    def partition_list(self, x):
        smaller_dummy = Node(0)
        larger_dummy = Node(0)
            
        smaller_temp = smaller_dummy
        larger_temp = larger_dummy
            
        temp = self.head
            
        while temp:
            if temp.value < x:
                smaller_temp.next = temp
                smaller_temp = temp
            else:
                larger_temp.next = temp
                larger_temp = temp
                
            temp = temp.next
            
        larger_temp.next = None
        smaller_temp.next = larger_dummy.next    

    # O(n)
    def remove_duplicates(self):
        values = set()
        
        prev = None
        current = self.head
            
        while current:
            if current.value not in values:
                values.add(current.value)
                prev = current
        
            else:
                prev.next = current.next
                self.length -= 1
                
            current = current.next

    # O(n), (num * 2) + b = Shift the existing value left by 1 bit (×2), then add the new value.
    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num

    def reverse_between(self, start_index, end_index):
        if self.length <= 1:
            return
    
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
    
        for i in range(start_index):
            previous_node = previous_node.next
    
        current_node = previous_node.next
    
        for i in range(end_index - start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move
    
        self.head = dummy_node.next

        
def find_kth_from_end(linked_list, k):
    slow = fast = linked_list.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    return slow




        
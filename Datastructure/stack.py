class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1
        return True

    def pop(self):
        if self.top is None:
            return None
        
        temp = self.top
        self.top = temp.next
        temp.next = None

        self.height -= 1
        return temp
    
def is_balanced_parentheses(parentheses):
    stack = Stack()
    
    for p in parentheses:
        if p == "(":
            stack.push(p)
        else:
            pair = stack.pop()
            if not pair:
                return False
            
    return stack.is_empty()

def reverse_string(string):
    stack = Stack()
    reversed_string = ""

    for char in string:
        stack.push(char)
    
    while not stack.is_empty():
        reversed_string += stack.pop()
        
    return reversed_string

def sort_stack(input_stack):
    sorted_stack = Stack()
    
    while not input_stack.is_empty():
        temp = input_stack.pop()
        
        while not sorted_stack.is_empty() and temp < sorted_stack.peek():
            input_stack.push(sorted_stack.pop())
            
        sorted_stack.push(temp)
            
    # Transfer all items from sorted to input_stack
    while not sorted_stack.is_empty():
        input_stack.push(sorted_stack.pop())
        
    return input_stack
    
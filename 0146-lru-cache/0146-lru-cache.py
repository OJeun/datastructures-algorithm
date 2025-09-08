from collections import deque 
class Node:
    def __init__(self, pair):
        self.pair = pair
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        if prev:
            prev.next = nxt
        else:
            self.head = nxt
        
        if nxt:
            nxt.prev = prev
        else:
            self.tail = prev
        
        node.next = None
        node.prev = None

        return node
    
    def pop(self): # remove head(the least accessed)
        popped = self.head
        if not self.head and not self.tail:
            return None

        nxt = self.head.next
        if not nxt:
            self.tail = None
            self.head = None
        else:
            self.head.next = None
            self.head.prev = None
            self.head = nxt
    
        return popped 

    def append(self, node): # pair = (key, value) => node is recent accessed
        node.prev = node.next = None 
        if not self.tail and not self.head:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        return node


class LRUCache:
    def __init__(self, capacity: int):
        self.data = dict() # key and node pointer
        self.dll = DoublyLinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        node = self.data.get(key)
        if node:
            value = node.pair[1]
            self.dll.remove(node)
            self.dll.append(node)
            self.data[key] = node
            return value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if self.data.get(key):
            node = self.data[key]
            node.pair[1] = value
            self.dll.remove(node)          
            self.dll.append(node)  
        
        else:
            if len(self.data) == self.capacity:
                moved_node = self.dll.pop()
                self.data.pop(moved_node.pair[0]) 
        
            added_node = self.dll.append(Node([key, value]))
            self.data[key] = added_node
class Node:
    def __init__(self, key:int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    # Insert the newest element to the first
    def add(self, key, val):
        new_node = Node(key, val)
        if self.first == None and self.last == None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node
        self.length += 1
        return new_node

    def update_order(self, recent_node):
        if recent_node != self.first:
            prev_node = recent_node.prev
            next_node = recent_node.next
            prev_node.next = next_node
            if next_node is not None:
                next_node.prev = prev_node
            else:
                self.last = prev_node
            self.first.prev = recent_node
            recent_node.next = self.first
            recent_node.prev = None
            self.first = recent_node
    
    def delete(self): # Delete the last node = oldest node
        node_to_delete = None
        if self.last == self.first:
            node_to_delete = self.first
            self.last = None
            self.first = None
        else:
            node_to_delete = self.last
            prev_node = self.last.prev
            prev_node.next = None
            self.last = prev_node 
        self.length -= 1

        return node_to_delete

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: val, value: node address
        self.deque = Deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.deque.update_order(node)
            return node.val
        else:
            return - 1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.deque.update_order(node)
        else:
            if self.deque.length >= self.capacity:
                node_to_delete = self.deque.delete()
                del self.cache[node_to_delete.key]
                
            added_node = self.deque.add(key, value)
            self.cache[key] = added_node
            
            

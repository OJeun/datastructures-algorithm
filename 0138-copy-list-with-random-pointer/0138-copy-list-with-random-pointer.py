class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        address_random_dict = dict()
        curr = head

        if curr == None:
            return curr

        while curr:
            copied_node = Node(curr.val, curr.next, curr.random)
            address_random_dict[curr] = copied_node
            curr = curr.next

        temp = head
        while temp:
            deep_copied = address_random_dict[temp]
            if temp.next:
                next_deep_copied = address_random_dict[temp.next]
                deep_copied.next = next_deep_copied
            if temp.random:
                random_deep_copied = address_random_dict[temp.random]
                deep_copied.random = random_deep_copied
            temp = temp.next

        new_head = address_random_dict[head]

        return new_head


                    
                    



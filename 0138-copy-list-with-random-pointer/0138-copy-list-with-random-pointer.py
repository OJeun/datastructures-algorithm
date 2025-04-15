class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        if curr is None:
            return None

        while curr:
            copied_node = Node(curr.val, curr.next, None)
            curr.next = copied_node
            curr = copied_node.next

        # original1 → copy1 → original2 → copy2 → original3 → copy3 → None
        
        temp = head
        new_head = temp.next

        # Change random to copied ones
        while temp:
            copied = temp.next
            if temp.random:
                copied.random = temp.random.next
            temp = temp.next.next

        temp = head
        # Change next
        while temp and temp.next:
            next_node = temp.next
            temp.next = next_node.next
            temp = next_node

        return new_head

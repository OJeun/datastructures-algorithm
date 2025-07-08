# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # slow, fast = head 
        slow, fast = head, head

        # move fast pointer n nodes ahead of head using for loop
        for _ in range(n):
            fast = fast.next
        
        if fast is None: # remove head
            next_node = head.next
            head.next = None
            head = next_node
            return head

        # traverse linked list until fast reach to the end
        while fast and fast.next:
            # increase fast and slow by 1
            fast = fast.next
            slow = slow.next

         # if slow == head: remove head node and move head pointer to the next      

        # remove a node next to slow
        to_be_removed = slow.next
        slow.next = to_be_removed.next
        to_be_removed.next = None

        # return head
        return head
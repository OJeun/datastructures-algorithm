# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        
        if not head or not head.next:
            return None

        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        if slow:
            slow.next = slow.next.next
        else:
            next_node = head.next
            head.next = None
            head = next_node

        return head

        
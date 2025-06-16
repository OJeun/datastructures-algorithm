# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        larger_dummy = ListNode()
        larger_temp = larger_dummy

        smaller_dummy = ListNode()
        smaller_temp = smaller_dummy

        while head:
            if head.val < x:
                smaller_temp.next = head
                smaller_temp = head

            else:
                larger_temp.next = head
                larger_temp = head

            head = head.next

        smaller_temp.next = larger_dummy.next
        larger_temp.next = None

        return smaller_dummy.next
            


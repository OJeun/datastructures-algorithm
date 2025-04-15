# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        smaller_ll = ListNode(0, None)
        larger_ll = ListNode(0, None)

        smaller_pointer = smaller_ll
        larger_pointer = larger_ll

        temp = head

        while temp:
            if temp.val < x:
                smaller_pointer.next = temp
                smaller_pointer = smaller_pointer.next
            else:
                larger_pointer.next = temp
                larger_pointer = larger_pointer.next
            temp = temp.next
            
        larger_pointer.next = None
        smaller_pointer.next = larger_ll.next
        head = smaller_ll.next

        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1
        temp = head
        tail = None

        if head == None or head.next == None:
            return head

        while temp.next:
            count += 1
            temp = temp.next
            if temp.next is None:
                tail = temp
        
        tail.next = head
        k %= count

        to_tail = head
        for _ in range(count - k - 1):
            to_tail = to_tail.next

        head = to_tail.next

        to_tail.next = None
        return head

        


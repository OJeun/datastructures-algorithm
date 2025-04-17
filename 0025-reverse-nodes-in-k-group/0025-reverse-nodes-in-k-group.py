# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        dummy.next = head

        curr = head
        reverse = None

        while curr:
            count = k
            tail = curr
            reverse = None

            temp = curr
            for _ in range(k):
                if temp:
                    count -= 1
                    temp = temp.next
                else:
                    break
                
            
            if count == 0:
                for _ in range(k):
                    next_node = curr.next
                    curr.next = reverse
                    reverse = curr
                    curr = next_node
                prev.next = reverse
                prev = tail
                tail.next = curr
            else:
                curr = curr.next if curr else None







        return dummy.next
            
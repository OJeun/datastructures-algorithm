# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # define slow and fast and initialize both to head
        slow, fast = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        second_half_head = None

        while temp:
            next_node = temp.next
            temp.next = second_half_head
            second_half_head = temp
            temp = next_node

        left = head
        right = second_half_head
        while left and right:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next
            
            right = right_next
            left = left_next
        
        return head

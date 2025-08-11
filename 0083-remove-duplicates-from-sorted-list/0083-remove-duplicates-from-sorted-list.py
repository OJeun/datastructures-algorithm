# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        duplicate = head

        while temp:
            duplicated_val = temp.val

            while duplicate and duplicate.val == duplicated_val:
                duplicate = duplicate.next
            
            temp.next = duplicate
            temp = duplicate

        return head
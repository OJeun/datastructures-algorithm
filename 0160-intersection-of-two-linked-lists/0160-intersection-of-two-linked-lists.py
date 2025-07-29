# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dummy_a = ListNode(0)
        dummy_b = ListNode(0)

        dummy_a.next = headA
        dummy_b.next = headB

        while headA and headB:
            if headA is headB:
                return headA

            headA = headA.next
            headB = headB.next

        if headA is None:
            headA = dummy_b.next
            while headB:
                headA = headA.next
                headB = headB.next
            headB = dummy_a.next

        if headB is None:
            headB = dummy_a.next
            while headA:
                headB = headB.next
                headA = headA.next
            headA = dummy_b.next
        
        if headA == headB:
            return headA

        while headA != headB:
            if not headA or not headB:
                return -1

            headA = headA.next
            headB = headB.next

            if headA is headB:
                return headA


        

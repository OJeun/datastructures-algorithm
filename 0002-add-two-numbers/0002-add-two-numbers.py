# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy
        added = 0

        while l1 and l2:
            two_sum = l1.val + l2.val + added
            added = 0
            if two_sum > 9:
                added = 1
                two_sum -= 10

            new_node = ListNode(two_sum)
            result.next = new_node
            result = result.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum_digit = added + l1.val
            added = 0
            if sum_digit > 9:
                added = 1
                sum_digit -= 10
            new_node = ListNode(sum_digit)
            result.next = new_node
            result = result.next
            l1 = l1.next

        while l2:
            sum_digit = added + l2.val
            added = 0
            if sum_digit > 9:
                added = 1
                sum_digit -= 10
            new_node = ListNode(sum_digit)
            result.next = new_node
            l2 = l2.next
            result = result.next

        if added:
            result.next = ListNode(1)

        return dummy.next

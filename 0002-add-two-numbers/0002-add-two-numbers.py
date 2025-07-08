# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Initailize carry variable to 0
        carry = 0
        dummy = ListNode()
        current = dummy

        # Use while loop until both stay in the boundary
        while l1 or l2 or carry:
            # calculate the sum of two digits and carry 
            first_val = l1.val if l1 else 0
            second_val = l2.val if l2 else 0
            sum_of_two_digits = first_val + second_val + carry
            # store that calculated value in new linked list
            new_node = ListNode(sum_of_two_digits % 10)
            current.next = new_node
            current = new_node
            # update the carry
            carry = sum_of_two_digits // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            new_digit = ListNode(1)
            current.next = new_digit

        return dummy.next




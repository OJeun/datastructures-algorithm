# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # define two pointers slow and fast initializing it to head
        slow, fast = head, head

        # while loop until fast reaches to the end of the list
        while fast and fast.next and fast.next.next:
            # move fast two steps, slow on step at once
            fast = fast.next.next
            slow = slow.next

        # make a new pointer(new_head) that points next node of slow and then slow.next points to None
        curr = slow.next
        slow.next = None

        temp = None
        # create curr pointer initiazliing it to new_head
        
        # while loop until curr exists => reverse the second half
        while curr:
            # prepend the current node to new_head
            next_node = curr.next
            curr.next = temp
            temp = curr
            curr = next_node

        # compare the first half with reversed second half
        while temp and head:
            # if they have different value
            if temp.val != head.val:
                return False
            temp = temp.next
            head = head.next

        return True
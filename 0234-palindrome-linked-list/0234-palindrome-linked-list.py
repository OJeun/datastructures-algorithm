class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = None

        while fast and fast.next:
            fast = fast.next.next

            if slow is None:
                slow = head
            else:
                slow = slow.next

        temp = None
        prev = slow
        curr = slow.next if slow else None
    
        while curr:
            next_node = curr.next

            curr.next = temp
            temp = curr
            curr = next_node

        left = head
        right = temp

        while right and left:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next

        return True


        
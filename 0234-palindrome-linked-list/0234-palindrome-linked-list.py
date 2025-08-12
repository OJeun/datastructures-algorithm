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

        if slow is None:
            return True

        curr = slow.next
        slow.next = None
        prev = None 
    
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            

        right = prev

        while right and head:
            if right.val != head.val:
                return False
            right = right.next
            head = head.next

        return True


        
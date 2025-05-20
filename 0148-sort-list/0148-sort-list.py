class Solution:
    def sortList(self, head):
        def merge(l1, l2):
            dummy_node = ListNode(0)
            tail = dummy_node

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            if l1:
                tail.next = l1
            if l2:
                tail.next = l2

            return dummy_node.next

        def helper(head):
            if head is None or head.next is None:
                return head

            slow = head
            fast = head
            prev = None

            while fast and fast.next:
                prev = slow
                fast = fast.next.next
                slow = slow.next

            prev.next = None

            left = helper(head)
            right = helper(slow)

            return merge(left, right)
            
        return helper(head)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        def get_kth_node(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        while True:
            kth = get_kth_node(prev, k)
            if not kth:
                break

            next_group = kth.next
            # reverse between prev.next and kth
            prev_curr = prev.next
            curr = prev_curr.next

            while curr != next_group:
                temp = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = temp

            prev_curr.next = next_group
            prev = prev_curr

        return dummy.next

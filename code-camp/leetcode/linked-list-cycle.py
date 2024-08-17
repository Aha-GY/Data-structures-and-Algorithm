class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast, slow = head,head
        if fast== None:
            return False
        elif fast.next:
            fast = fast.next.next
        else:
            return False
        slow = slow.next
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        if fast == slow:
            return True
        return False
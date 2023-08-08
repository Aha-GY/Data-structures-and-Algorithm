class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == 10**6:
                return True
            head.val = 10**6
            head = head.next
        return False
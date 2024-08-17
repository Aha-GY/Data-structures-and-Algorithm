class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            head = None
            return head
        slow = head
        fast = head
        previous = head
      
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            previous = slow
            slow = slow.next
        if slow == head:
            head = slow.next   
        if previous:
            previous.next = slow.next
        
        return head
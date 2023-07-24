
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        left = ListNode() 
        right = ListNode()  
        left_tail = left  
        right_tail = right 
 
        while head:
            if head.val >= x:
                right_tail.next = head
                right_tail = right_tail.next
            else:
                left_tail.next = head
                left_tail = left_tail.next
            head = head.next

        left_tail.next = right.next
        right_tail.next = None
        return left.next

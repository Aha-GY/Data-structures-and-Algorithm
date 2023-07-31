class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        leftprev , cur = dummy , head
        for i in range(left-1):
            leftprev , cur = cur , cur.next
        
        pre = None
        for i in range(right-left+1):
            tmp = cur.next
            cur.next = pre
            pre , cur = cur , tmp
        
        leftprev.next.next = cur
        leftprev.next = pre
        
        return dummy.next
                
        
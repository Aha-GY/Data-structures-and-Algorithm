class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        char = head 
        prev = None 
        while char:
            next = char.next
            char.next = prev
            prev = char
            char = next
        return prev
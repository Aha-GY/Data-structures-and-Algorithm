# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return True
        
        else:
            # find the midel 
            slow = head
            fast = head
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            # rivers the second half 
            prev =  None 
            current  = slow
            while current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            # compiar the first half and the second half
            
            j = head
            i = prev
            while i :
                if i.val != j.val:
                    return False
                i = i.next
                j = j.next
            return True
            
                
                
        
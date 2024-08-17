class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return head
        
        prev = head 
        current = head.next  
        
        while current:
            if prev.val == current.val:
                prev.next = current.next 
            else:
                prev = current  
            current = current.next 
        
        return head

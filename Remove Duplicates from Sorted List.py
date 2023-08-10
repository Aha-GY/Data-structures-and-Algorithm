class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return head
        curr = head
        while curr.next != None:
            if curr.val == curr.next.val:
                tmp = curr.next
                curr.next = curr.next.next
                del tmp
            else:
                curr = curr.next
        return head        
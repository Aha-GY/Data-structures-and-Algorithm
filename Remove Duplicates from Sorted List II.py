class Solution(object):
    def deleteDuplicates(self, head):
        fake = ListNode(-1)
        fake.next = head
        # We use prev (for node just before duplications begins), curr (for the last node of the duplication group)...
        curr, prev = head, fake
        while curr:
            
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next
        return fake.next
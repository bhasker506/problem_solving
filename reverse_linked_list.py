class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 5->4->3->2->1-null
class Solution:
    
    def reverse_linked_list(self, head):
        if not head:
            return
        previous = None
        while head:
            next = head.next
            head.next = previous
            previous = head
            head = next
        return previous
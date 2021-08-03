# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
    
    def fast_half_end(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head:
            return True
        
        end_fast_half = self.fast_half_end(head=head)
        second_half_start = end_fast_half.next
        
        first_position = head
        second_position = self.reverse_list(second_half_start)
        
        while second_position:
            if first_position.val != second_position.val:
                return False
            second_position = second_position.next
            first_position = first_position.next
        
        return True

if __name__ == '__main__':
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    head.next.next = ListNode(val=2)
    head.next.next.next = ListNode(val=1)
    s = Solution()
    print(s.isPalindrome(head=head))
    
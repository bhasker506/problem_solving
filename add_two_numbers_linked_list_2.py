class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def reverse_list(self, head: ListNode) -> ListNode:
        if not head:
            return
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
    
    def addTwoNumbersReverse(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return
        
        rev_l1 = self.reverse_list(head=l1)
        rev_l2 = self.reverse_list(head=l2)
        
        carry = 0
        head = ListNode()
        result = head
        while rev_l1 or rev_l2:
            val = carry
            if l1:
                val += l1.val
            if l2:
                val += l2.val
            if val >= 10:
                carry = 1
                val %= 10
            result.next = ListNode(val=val)
            result = result.next
            rev_l1 = rev_l1.next if rev_l1 else None 
            rev_l2 = rev_l2.next if rev_l2 else None
        
        if carry>0:
            result.next = ListNode(val=carry)
        
        return self.reverse_list(head.next)
        
             
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # find the length of both lists
        n1 = n2 = 0
        curr1, curr2 = l1, l2
        while curr1:
            curr1 = curr1.next 
            n1 += 1
        while curr2:
            curr2 = curr2.next 
            n2 += 1
            
        # parse both lists
        # and sum the corresponding positions 
        # without taking carry into account
        # 3->3->3 + 7->7 --> 3->10->10 --> 10->10->3
        curr1, curr2 = l1, l2
        head = None
        while n1 > 0 and n2 > 0:
            val = 0
            if n1 >= n2:
                val += curr1.val 
                curr1 = curr1.next 
                n1 -= 1
            if n1 < n2:
                val += curr2.val 
                curr2 = curr2.next
                n2 -= 1
                
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

        # take the carry into account
        # to have all elements to be less than 10
        # 10->10->3 --> 0->1->4 --> 4->1->0
        curr1, head = head, None
        carry = 0
        while curr1:
            # current sum and carry
            val = (curr1.val + carry) % 10
            carry = (curr1.val + carry) // 10
            
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

            # move to the next elements in the list
            curr1 = curr1.next
        
        # add the last carry
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head
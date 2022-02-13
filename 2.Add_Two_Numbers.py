# Thanks Patrick Oweijane for this wonderful solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, head = 0, l1
        #Let l1 be the list we will return, and keep replacing values on l1. if not l1.next and l2: l1.next, l2.next = l2.next, l1.next means that whenever we reach the tail of l1, but did not reach the end of l2 yet, we will swap the links so that l1 becomes the longer list.
        
        while l1 or l2:
            if not l1.next and l2:
                l1.next, l2.next = l2.next, l1.next
            
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            carry, l1.val = divmod(l1_val + l2_val + carry, 10)

            #Keep Track of l1 node where we have to add carry node 
            prev = l1
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        if carry: prev.next = ListNode(carry)
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = []
        num2 = []
        while l1:
            num.append(l1.val)
            l1 = l1.next
        
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        
        li = []
        for i in range(len(num)):
            val = num[i] + num2[i]
            
            carry = 0
            if val >= 10:
                carry = 1
                val = val % 10
                
                if i != len(num)-1:
                    num[i+1] += 1
                    li.append(val)
                elif i == len(num)-1:
                    li.append(1)
            else:
                li.append(val)
        
        dummy = ListNode(0)
        node = dummy
        
        # *
        for x in li:
            node.next = ListNode(x)
            node = node.next
            
        return dummy.next
        
            
            
            

# 방법
# 1. 리스트
# 2. Deque 이용
# 3. 런너 이용

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. 리스트 이용
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li = []
        while head:
            li.append(head.val)
            head = head.next
        
        if li == li[::-1]:
            return True
        else:
            return False
          
# 2. Deque 이용
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dq = deque()
        while head:
            dq.append(head.val)
            head = head.next
        
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        
        return True
            

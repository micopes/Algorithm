# 방법
# 1. deque 이용
from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        dq = deque()
        for c in s:
            if '0' <= c <= '9' or 'a' <= c <= 'z':
                dq.append(c)
            elif 'A' <= c <= 'Z':
                dq.append(c.lower())
        
        while len(dq) > 1:
            if dq.pop() != dq.popleft():
                return False
        return True
    
# 2. 단순 검사.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_list = []
        for c in s:
            if '0' <= c <= '9' or 'a' <= c <= 'z':
                str_list.append(c)
            elif 'A' <= c <= 'Z':
                str_list.append(c.lower())
        
        string = "".join(str_list)
        string2 = string[::-1]
    
        if string == string2:
            return True
        else:
            return False
                

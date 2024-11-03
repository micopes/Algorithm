from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = deque()
        for c in s:
            if c.isalnum():
                string.append(c.lower())
        
        while len(string) > 1:
            if string.popleft() != string.pop():
                return False
        
        return True

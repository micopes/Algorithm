# 대소문자 주의
# 대문자, 소문자로 변경 : upper(), lower()
# 대문자, 소문자 판별 : isupper(), islower()
# 숫자, 문자 판별 : isalnum()
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_list = list(s)
        
        temp_string = ""
        for c in temp_list:
            if 'a' <= c <= 'z' or '0' <= c <= '9':
                temp_string += c
            elif 'A' <= c <= 'Z':
                temp_string += c.lower()
        
        print(temp_string)
        if temp_string == temp_string[::-1]:
            return True
        else:
            return False
        
        
# 풀이 2 덱을 이용한 풀이. - 더 빠름.
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
    
# 풀이 3. 정규표현식 이용.
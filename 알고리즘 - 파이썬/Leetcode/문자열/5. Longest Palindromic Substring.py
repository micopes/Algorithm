# palindrome 중앙에서 확장시켜간다 (짝수, 홀수) 나눠서.
# index 처리 주의 s = '12345'일 때 s[1:3]은 23이지만, s[3]은 4이다.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        result = s[0]
        for i in range(len(s)):
            result = max(result, expand(i, i+1), expand(i, i+2), key = len)
        return result
    
    
    
            
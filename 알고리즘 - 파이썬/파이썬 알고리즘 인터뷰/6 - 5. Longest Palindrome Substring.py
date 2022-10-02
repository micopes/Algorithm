class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
        
            return s[left+1:right]
    
        result = s[0]
        for i in range(len(s)):
            result = max(result, expand(i, i+1), expand(i, i+2), key = len)
            
        
        return result
            

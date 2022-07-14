class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        string = str(x)
        rev_string = string[::-1]
        if string == rev_string:
            return True
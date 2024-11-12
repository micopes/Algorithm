class Solution:
    def hammingWeight(self, n: int) -> int:
        ret_val = 0
        
        while n > 0:
            if n % 2 == 1:
                ret_val += 1
            n //= 2 
        
        return ret_val

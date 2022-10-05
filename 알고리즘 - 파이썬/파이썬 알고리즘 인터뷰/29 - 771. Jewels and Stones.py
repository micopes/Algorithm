class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        for c in stones:
            if c in jewels:
                result += 1
        
        return result
                
                

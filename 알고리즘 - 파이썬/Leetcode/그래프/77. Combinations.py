from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l = []
        for i in range(1, n+1):
            l.append(i)
        return list(combinations(l, k))
        

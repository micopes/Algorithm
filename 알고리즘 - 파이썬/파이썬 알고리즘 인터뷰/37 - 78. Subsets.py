# 방법
# 1. from itertools import combinations 사용
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        for i in range(len(nums)+1):
            for x in combinations(nums, i):
                result.append(x)
        
        return result
        
# 2. 직접 구현
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx, temp):
            if len(temp) <= len(nums):
                result.append(temp)
            else:
                return
            
            for i in range(idx, len(nums)):
                dfs(i+1, temp + [nums[i]])
                
                
            
        result = []
        
        dfs(0, [])
        return result

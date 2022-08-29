from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx, li, n):
            if len(li) == n:
                results.append(li)
                return
            
            for i in range(idx, len(nums)):
                if nums[i] not in li:
                    dfs(i, li + [nums[i]], n)

        results = []
        for i in range(len(nums)+1):
            dfs(0, [], i)
                 
        return results
        

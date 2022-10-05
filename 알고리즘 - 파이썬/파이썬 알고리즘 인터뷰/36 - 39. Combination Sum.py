import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, candidate, total):
            if total > target:
                return
            elif total == target:
                result.append(candidate)
            else:
                for i in range(idx, len(candidates)):
                    x = candidates[i]
                    dfs(i, candidate + [x], total + candidates[i])
        
        result = []
        dfs(0, [], 0)
        return result
        
        
        
        
        

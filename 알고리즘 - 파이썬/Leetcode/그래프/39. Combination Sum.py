class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, l, val):
            if val > target:
                return
            elif val == target:
                results.append(l)
                return
        
            # 순서에 따라 넣고, 정렬 등이 불필요하도록
            for i in range(idx, len(candidates)):
                x = candidates[i]
                dfs(i, l + [x], val + x)
        
        results = []
        dfs(0, [], 0)
        return results

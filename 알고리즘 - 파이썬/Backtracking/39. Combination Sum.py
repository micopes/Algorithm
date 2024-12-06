class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(idx, arr, sum_arr):
            if target == sum_arr:
                result.append(arr[:])
                return 
            
            for i in range(idx, len(candidates)):
                new_total = sum_arr + candidates[i]

                # 불필요한 것 넣지 않기 위해
                if new_total > target:
                    return

                arr.append(candidates[i])
                backtracking(i, arr, new_total)
                arr.pop()

        # main
        candidates.sort()
        result = []

        backtracking(0, [], 0)

        return result

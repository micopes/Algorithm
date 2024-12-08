class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start_idx, arr, sum_arr):
            if sum_arr == target:
                result.append(arr[:])
                return 

            for i in range(start_idx, len(candidates)):
                # 예제 입력 [1, 1]을 상상해보면 됨. 이걸 넣으면 마지막에 전체 중복 처리 안해도 됨.
                if start_idx < i and candidates[i-1] == candidates[i]:
                    continue

                new_total = sum_arr + candidates[i]
                if new_total > target:
                    break
                
                if visited[i] == False:
                    visited[i] = True
                    arr.append(candidates[i])
                    backtrack(i+1, arr, new_total)
                    visited[i] = False
                    arr.pop()

        result = []
        candidates.sort()
        visited = [0 for _ in range(len(candidates))]
        backtrack(0, [], 0)

        return result

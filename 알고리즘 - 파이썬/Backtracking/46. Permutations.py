class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(arr):
            if len(arr) == len(nums):
                result.append(arr[:])
                return

            for i in range(len(nums)):
                if visited[i] == False:
                    visited[i] = True
                    arr.append(nums[i])
                    backtrack(arr)
                    visited[i] = False
                    arr.pop() # 이것으로 permutation 완성

        result = []
        visited = [0 for _ in range(len(nums))]
        backtrack([])
        
        return result

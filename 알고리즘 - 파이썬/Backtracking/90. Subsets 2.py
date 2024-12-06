class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start_idx, arr, max_size):
            if len(arr) == max_size:
                result.append(tuple(arr[:]))
            
            for i in range(start_idx, len(nums)):
                if visited[i] == False:
                    visited[i] = True
                    arr.append(nums[i])
                    backtrack(i+1, arr, max_size)
                    visited[i] = False
                    arr.pop()

        result = []
        visited = [0 for _ in range(len(nums))]
        nums.sort()
        for i in range(len(nums)+1):
            backtrack(0, [], i)

        return list(set(result))
        

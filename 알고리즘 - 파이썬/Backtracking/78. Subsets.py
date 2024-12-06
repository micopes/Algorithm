class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def func(idx, x, max_size):
            if x == max_size:
                subsets = []
                for i in range(len(visited)):
                    if visited[i]:
                        subsets.append(nums[i])
                result.append(subsets)
                return 
            
            for i in range(idx, len(nums)):
                if visited[i] == False:
                    visited[i] = True
                    func(i+1, x+1, max_size)
                    visited[i] = False
        
        result = []
        for i in range(len(nums)+1):
            visited = [0 for _ in range(len(nums))]
            func(0, 0, i)

        return result
        

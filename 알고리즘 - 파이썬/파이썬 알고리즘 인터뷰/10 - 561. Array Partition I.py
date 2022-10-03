nums = [1, 4, 3, 2]

class Solution:
    def solution(self, nums) -> int:
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
            
        return result

import copy
class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        # 1. 누적합 응용
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]

        return max(nums)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        val = 1
        for i in range(len(nums)):
            result.append(val)
            val *= nums[i]
        
        val = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= val
            val *= nums[i]
        
        return result

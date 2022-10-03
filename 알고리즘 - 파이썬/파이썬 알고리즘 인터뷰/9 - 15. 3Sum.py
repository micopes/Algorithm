# 방법
# 1. 3중 for문
# 2. from itertools import combinations
# 3. dictionary
# 4. two pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(1, len(nums)-1):
            left = 0
            right = len(nums)-1
            while left < i and i < right:
                val = nums[left] + nums[i] + nums[right]
                if val == 0:
                    if [nums[left], nums[i], nums[right]] not in result:
                        result.append([nums[left], nums[i], nums[right]])
                    left += 1
                    right -= 1
                elif val < 0:
                    left += 1
                else: 
                    right -= 1
                    
        return result
            
        
        
                
                
        

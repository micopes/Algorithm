class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 방법 1. 이중 for loop를 이용해서 답을 구하는 방식 - O(n^2)
        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # 방법 2. x + y = target 딕셔너리 이용하면 된다.
        dic = {}
        for index, value in enumerate(nums):
            if target-value in dic:
                return [dic[target-value], index]
            dic[value] = index

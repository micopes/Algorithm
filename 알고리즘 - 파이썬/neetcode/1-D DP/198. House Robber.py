class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP
        # 1. 초기값
        dp = [0 for _ in range(len(nums))] # 0 ~ len(nums)-1
        dp[0] = nums[0]
        if len(nums) >= 2:
            dp[1] = max(nums[0], nums[1])
        
        # 2. 증감식
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        # 3. 결과값
        return dp[-1]
        

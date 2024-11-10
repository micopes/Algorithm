class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        # - 1, 2 계단을 오를 수 있는 방법

        dp = [0 for _ in range(n+3)] # 0 ~ n
        # 1. 초기값 - 초기값 설정 시 n이 0과 같은 낮은 숫자가 아닌지 확인.
        dp[1] = 1
        dp[2] = 2 # (1, 1), (2)
        
        # 2. 증감식
        for i in range(3, n+1):
            dp[i] += dp[i-1]
            dp[i] += dp[i-2]
        
        # 3. 결과값
        return dp[n]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m: 행 / n: 열
        
        # DP
        # 1. 초기값
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        
        # 2. 증감식
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += dp[i-1][j]
                dp[i][j] += dp[i][j-1]

        # 3. 결과값
        return dp[m-1][n-1]

        

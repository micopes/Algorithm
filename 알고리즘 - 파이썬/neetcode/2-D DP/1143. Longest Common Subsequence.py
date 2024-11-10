class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 공통의 Subsequence를 구하는 것이므로, 공통적으로 겹치는 부분을 찾아야 함.
        # 2-D DP
        dp = [[0]*(len(text2)) for _ in range(len(text1))]

        # 1. 초기값
        if text1[0] == text2[0]:
            dp[0][0] = 1

        for i in range(1, len(text1)):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i-1][0]

        for i in range(1, len(text2)):
            if text1[0] == text2[i]:
                dp[0][i] = 1
            else:
                dp[0][i] = dp[0][i-1]

        # 2. 증감식
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # 3. 결과값
        return dp[-1][-1]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 문제
        # 1. 한 계단 혹은 두 계단을 오를 수 있다.
        # 2. 0번 혹은 1번 계단에서 출발할 수 있다.
        # +) 계단 위 옥상이 있는 느낌..

        # DP
        # 1. 초기값
        dp = [0 for _ in range(len(cost)+1)] # 0 ~ len(cost)-1
        dp[0] = 0
        dp[1] = 0

        # 2. 증감식
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        # 3. 결과값
        return dp[-1]

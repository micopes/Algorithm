import sys
# input = sys.stdin.readline

D = int(input().rstrip())

dp = [0, 1, 0, 0, 0, 0, 0, 0, 0] # 1 ~ 8만 사용

for _ in range(D):
    temp = [0 for _ in range(9)]
    
    # n-1을 n 번째로 만드는 것
    temp[1] = dp[2] + dp[3]
    temp[2] = dp[1] + dp[3] + dp[4]
    temp[3] = dp[1] + dp[2] + dp[4] + dp[5]
    temp[4] = dp[2] + dp[3] + dp[5] + dp[6]
    temp[5] = dp[3] + dp[4] + dp[6] + dp[7]
    temp[6] = dp[4] + dp[5] + dp[8]
    temp[7] = dp[5] + dp[8]
    temp[8] = dp[6] + dp[7]
    
    # n 번째
    for i in range(1, 9):
        dp[i] = temp[i] % 1000000007

print(dp[1])
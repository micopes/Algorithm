n = int(input()) # 1 ~ 100

dp = [[0]*101 for _ in range(101)]

# 1. 초기값
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
dp[2] = [1, 1, 2, 2, 2, 2, 2, 2, 2, 1]
    
# 2. 점화식
for i in range(3, n+1):
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]


print( (sum(dp[n])) % 1000000000 )


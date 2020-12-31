n = int(input()) # 1 ~ 100

dp = [[0]*101 for _ in range(101)]

# dp[1] = 9 # 1, 2, 3, 4, 5, 6, 7, 8, 9
# dp[2] = 17  # 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89,  98

# 1. 초기값
for i in range(1, 10):
    dp[1][i] = 1 # dp[1][0]은 0

for i in range(2, 9):
    dp[2][i] = 2 # dp[2][0] = 1, dp[2][9] = 1
    
dp[2][1] = 1 # 맨처음에 0이 나올 수 없기 때문
dp[2][0] = 1
dp[2][9] = 1

# 2. 점화식
for i in range(3, n+1):
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

# 최종 결과
# result = dp[n-1][0] + dp[n-1][1]...
result = 0
for i in range(0, 10):
    result += dp[n][i]
    result %= 1000000000

print(result)


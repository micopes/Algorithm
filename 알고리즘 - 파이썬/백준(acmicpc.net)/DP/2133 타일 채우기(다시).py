n = int(input()) # n : 1 ~ 30

dp = [0 for _ in range(31)] # 1 ~ 30

# 초기값
dp[0] = 1
dp[2] = 3
dp[4] = 11

# 점화식
for i in range(1, 30, 2):
    dp[i] = 0
for i in range(6, 31, 2):
    dp[i] = dp[i-2] * 3
    for j in range(4, i+1, 2):
        dp[i] += dp[i-j] * 2
# 결과
print(dp[n])
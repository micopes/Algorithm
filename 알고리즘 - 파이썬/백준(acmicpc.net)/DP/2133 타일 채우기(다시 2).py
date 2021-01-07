n = int(input())

dp = [0 for _ in range(31)] # 1 ~ 30

dp[2] = 3
dp[4] = 11

for i in range(6, 31, 2):
    dp[i] = dp[i-2] * 3
    for j in range(4, i, 2):
       dp[i] += dp[i-j] * 2
    dp[i] += 2

print(dp[n])
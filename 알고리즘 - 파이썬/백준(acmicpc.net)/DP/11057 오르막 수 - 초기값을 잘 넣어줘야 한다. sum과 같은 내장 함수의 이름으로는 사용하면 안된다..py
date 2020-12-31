n = int(input())

dp = [[0]*10 for _ in range(1001)] # [1001][10]

dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 0 ~ 9

for i in range(2, n+1):
    for j in range(10):
        for k in range(j+1): # 0 ~ j
            dp[i][j] += dp[i-1][k]
            
print(sum(dp[n]) % 10007)

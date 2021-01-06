import sys

n, k = map(int, sys.stdin.readline().split())

dp = [[0]*201 for _ in range(201)] # [200][200]

for i in range(201):
    dp[i][1] = 1 # 1개 더해서 i를
    
for i in range(201):
    dp[1][i] = i # k개 더해서 1

    
for i in range(2, 201):
    for j in range(2, 201):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp[i][j] %= 1000000000
        
print(dp[n][k])

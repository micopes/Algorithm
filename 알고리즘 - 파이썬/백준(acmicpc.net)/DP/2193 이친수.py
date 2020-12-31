n = int(input())

dp = [[0]*2 for _ in range(91)] # [91][0], [91][1]

dp[1][0] = 0 # 0으로 끝나는 1자리 이친수
dp[1][1] = 1 # 1로 끝나는 1자리 이친수

for i in range(2, 91):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
    
print(dp[n][0] + dp[n][1])
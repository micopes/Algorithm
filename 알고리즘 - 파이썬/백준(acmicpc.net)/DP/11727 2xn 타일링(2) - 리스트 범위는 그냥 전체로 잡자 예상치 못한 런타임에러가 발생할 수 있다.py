n = int(input())

dp = [0 for _ in range(1001)]

# 1. 초기값
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-1] + 2*dp[i-2]
    dp[i] %= 10007
    
print(dp[n])
    
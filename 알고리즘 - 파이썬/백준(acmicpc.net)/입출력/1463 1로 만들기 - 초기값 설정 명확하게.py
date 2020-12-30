n = int(input())


dp = [0 for _ in range(n+1)]

# 1. 초기값 설정
dp[1] = 0

# 2. 점화식
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])
    
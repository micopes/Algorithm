import sys

# sys.stdin.readline()
n = int(input())

cards = list(map(int, input().split()))

# 초기값
dp = cards[:] # Deep Copy
dp.insert(0, 0)

for i in range(2, n+1): # 2 ~ n
    for j in range(i//2+1): # 1 ~ i/2
        dp[i] = max(dp[i-j] + dp[j], dp[i])

print(dp[n])




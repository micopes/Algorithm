dp = [0 for _ in range(100001)] # 1 ~ 100000

n = int(input())
for i in range(n+1):
    dp[i] = i


num = 0
for num in range(1, 10000):
    if num**2 > n+1:
        break

for i in range(n+1):
    for j in range(num+1):
        if i - j**2 >= 0:
            dp[i] = min(dp[i-j**2]+1, dp[i])

print(dp[n])

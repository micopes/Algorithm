n = int(input())
a = list(map(int, input().split()))

dp = [0 for _ in range(n)]

# dp = 연결된 과거를 고려해서 
# 해당 숫자에서 최댓값이 되는.
dp[0] = a[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+a[i], a[i])

print(max(dp))
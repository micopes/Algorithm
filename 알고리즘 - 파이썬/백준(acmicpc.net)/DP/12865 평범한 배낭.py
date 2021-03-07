import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

# 1 ~ n
w = [0]
v = [0]
dp = [[0]*(k+1) for _ in range(n+1)] # [n][k] 까지

for i in range(n):
    wTemp, vTemp = map(int, input().rstrip().split())
    w.append(wTemp)
    v.append(vTemp)

for i in range(1, n+1):
    for j in range(1, k+1):
        if w[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

print(dp[n][k])
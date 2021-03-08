import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

importance = [0]
needTime = [0]
for i in range(k):
    imp, time = map(int, input().rstrip().split())
    importance.append(imp)
    needTime.append(time)

dp = [[0]*(n+1) for _ in range(k+1)] # [n][k]

for i in range(1, k+1):
    for j in range(1, n+1):
        if needTime[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-needTime[i]] + importance[i])

print(dp[k][n])
        
import sys
# input = sys.stdin.readline

n, t = map(int, input().rstrip().split())

# index : 1 ~  
K = [0]
S = [0]
for i in range(n):
    kTemp, sTemp = map(int, input().rstrip().split())
    K.append(kTemp)
    S.append(sTemp)

dp = [[0]*(t+1) for _ in range(n+1)] # [n][k]

for i in range(1, n+1):
    for j in range(1, t+1):
        if K[i] > j :
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-K[i]] + S[i])
print(dp[n][t])
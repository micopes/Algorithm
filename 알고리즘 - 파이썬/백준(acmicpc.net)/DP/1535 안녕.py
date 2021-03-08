import sys
input = sys.stdin.readline

n = int(input().rstrip())

health = [0] + list(map(int, input().rstrip().split()))
joy = [0] + list(map(int, input().rstrip().split()))

dp = [[0]*100 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, 100):
        if health[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-health[i]] + joy[i])

print(dp[n][99])
            
        

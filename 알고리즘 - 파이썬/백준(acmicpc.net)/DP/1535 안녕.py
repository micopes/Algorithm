import sys
# input = sys.stdin.readline

n = int(input().rstrip())

now = 100
health = [0]
joy = [0]
healthTemp = list(map(int, input().rstrip().split()))
joyTemp = list(map(int, input().rstrip().split()))
for i in range(len(healthTemp)):
    health.append(healthTemp[i])
    joy.append(joyTemp[i])

dp = [[0]*100 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, 100):
        if health[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-health[i]] + joy[i])

print(dp[n][99])
            
        

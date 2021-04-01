import sys
# input = sys.stdin.readline 

n, m = map(int, input().rstrip().split())

coin = []
for i in range(n):
    x = int(input().rstrip())
    coin.append(x)

dp = [10001]*10001

dp[0] = 0
for x in coin:
    dp[i] = 1

for i in range(n):
    for j in range(coin[i], m+1):
        dp[j] = min(dp[j], dp[j-coin[i]] + 1)

if dp[m] == 10001:
    print("-1")
else:
    print(dp[m])
        
        
        





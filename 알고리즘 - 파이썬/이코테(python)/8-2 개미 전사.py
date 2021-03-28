import sys
# input = sys.stdin.readline

n = int(input().rstrip())

food = list(map(int, input().rstrip().split())) # 0 ~ n-1
dp = [0 for _ in range(101)]
dp[0] = food[0]
dp[1] = max(food[0], food[1]) # dp[0], food[1]
dp[2] = max(food[1], dp[0] + food[2]) # dp[0] + food[2], food[1]

for i in range(3, n):
    dp[i] = max(dp[i-3] + food[i-1], dp[i-2] + food[i])

print(dp[n-1])
    
    
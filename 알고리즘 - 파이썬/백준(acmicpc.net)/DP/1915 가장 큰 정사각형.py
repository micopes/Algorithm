import sys
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

graph = []

for i in range(n):
    graph.append(list(map(int, list(input().rstrip()))))

dp = [[0]*m for i in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = graph[i][j]
        elif graph[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        ans = max(dp[i][j], ans)
        
print(ans*ans)

    
    
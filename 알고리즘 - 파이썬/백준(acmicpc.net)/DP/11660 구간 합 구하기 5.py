import sys
input = sys.stdin.readline

n, t = map(int, input().rstrip().split())

board = []
for i in range(n):
    board.append(list(map(int, input().rstrip().split())))

dp = board[:]
for i in range(1, n):
    dp[i][0] = dp[i][0] + dp[i-1][0]
    dp[0][i] = dp[0][i] + dp[0][i-1]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    if x1 == 0 and y1 == 0:
        ans = dp[x2][y2]
    elif x1 == 0:
        ans = dp[x2][y2] - dp[x2][y1-1]
    elif y1 == 0:
        ans = dp[x2][y2] - dp[x1-1][y2]
    else:
        ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
            
    print(ans)
    
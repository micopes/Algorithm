import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def backtrack(x, y, visitedAlpha, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visitedAlpha:
                visitedAlpha += board[nx][ny]
                backtrack(nx, ny, visitedAlpha, cnt+1)
                visitedAlpha = visitedAlpha[:-1]
                
# [행][열]
R, C = map(int, input().rstrip().split())
board = [] # [0~R-1][0~C-1]
for i in range(R):
    string = input().rstrip()
    board.append(list(string))

# 좌측 상단 처리
visitedAlpha = ""
visitedAlpha += board[0][0]
ans = 1

backtrack(0, 0, visitedAlpha, 1)

print(ans)




    
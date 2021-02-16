import sys
# input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def backtrack(x, y, visitedAlpha, cnt):
    global ans
    if cnt > ans:
        ans = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if visited[nx][ny] == 0 and board[nx][ny] not in visitedAlpha:
                visited[nx][ny] = 1
                visitedAlpha.append(board[nx][ny])
                backtrack(nx, ny, visitedAlpha, cnt+1)
                visited[nx][ny] = 0
                visitedAlpha.pop()
                

# [행][열]
R, C = map(int, input().rstrip().split())
board = [] # [0~R-1][0~C-1]
for i in range(R):
    string = input().rstrip()
    board.append(list(string))
    
visited = [[0]*C for _ in range(R)] # [R-1][C-1]

# 좌측 상단 처리
visited[0][0] = 1
visitedAlpha = [board[0][0]]
ans = 1
backtrack(0, 0, visitedAlpha, 1)

print(ans)




    
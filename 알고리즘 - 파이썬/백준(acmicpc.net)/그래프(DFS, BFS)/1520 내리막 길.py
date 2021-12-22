import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def route(x, y):
    if x == ROW-1 and y == COL-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < ROW and 0 <= ny < COL:
            if board[nx][ny] < board[x][y]:
                visited[x][y] += route(nx, ny)
    
    return visited[x][y]

ROW, COL = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(ROW)]

visited = [[-1]*COL for _ in range(ROW)]

ans = route(0, 0)
print(ans)


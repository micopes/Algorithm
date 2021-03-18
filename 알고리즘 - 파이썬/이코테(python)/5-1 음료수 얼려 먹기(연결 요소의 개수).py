import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10**6) 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global ans
    visited[x][y] = ans
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and graph[nx][ny] == '0':
                visited[nx][ny] = ans
                dfs(nx, ny)
    
    
n, m = map(int, input().rstrip().split())
graph = []
for i in range(n):
    string = input()
    graph.append(list(string))

visited = [[0]*m for _ in range(n)] # [n-1][m-1]

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0' and visited[i][j] == 0:
            ans += 1
            dfs(i, j)
            
        
print(ans)
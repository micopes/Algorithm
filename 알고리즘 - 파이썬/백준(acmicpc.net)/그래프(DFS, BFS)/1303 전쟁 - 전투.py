# N, M : 열, 행 - [M][N]
import sys
from collections import deque

def bfs(ch, i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == ch:
                q.append([nx, ny])
                visited[nx][ny] = 1
                cnt += 1
    return cnt**2
                
n, m = map(int, input().split())
visited = [[0]*n for _ in range(m)]
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
W_score = 0
B_score = 0


for i in range(m):
    graph.append(list(input()))
    
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and visited[i][j] == 0:
            W_score += bfs('W', i, j)
        elif graph[i][j] == 'B' and visited[i][j] == 0:
            B_score += bfs('B', i, j)

print(W_score, B_score)
    
    

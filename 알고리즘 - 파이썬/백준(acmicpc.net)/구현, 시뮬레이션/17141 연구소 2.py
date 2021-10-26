import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(selected):
    q = deque()
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                visited[i][j] = -1
                
    # 마지막에 1 감소 필요
    for i, j in selected:
        q.append([i, j])
        visited[i][j] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    max_val = -1
    
    # 0이 존재한다면
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                return sys.maxsize
            
    # 0이 존재하지 않는다면 걸린 시간(가장 마지막에 채워진 것)        
    for i in range(n):
        for j in range(n):
            max_val = max(max_val, visited[i][j])
    
    return max_val
    
        

n, m = map(int, input().rstrip().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))
    
# 바이러스를 놓을 수 있는 위치
location = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            location.append([i, j])

ans = sys.maxsize
# 바이러스를 놓을 수 있는 위치에서 m개를 뽑아 selected.
for selected in combinations(location, m):
    ans = min(ans, bfs(selected))

if ans == sys.maxsize:
    print(-1)
else:
    print(ans-1)

    
            
    

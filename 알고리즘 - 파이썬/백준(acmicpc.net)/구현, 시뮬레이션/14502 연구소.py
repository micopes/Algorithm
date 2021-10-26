import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(selected):
    visited = [[0]*m for _ in range(n)]
    
    # 빈 칸에 벽을 세울 수 있다 (3개)
    for r, c in selected:
        # 벽 : -1
        visited[r][c] = -1 
    
    q = deque()
    for i in range(n):
        for j in range(m):
            # 바이러스 : 1
            if graph[i][j] == 2:
                q.append([i, j])
                visited[i][j] = 1
            # 벽 : -1
            elif graph[i][j] == 1:
                visited[i][j] = -1
            # 빈 칸 : 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])
    
    ret = 0
    # 바이러스가 모두 퍼지고 최종 0의 개수 : 안전 영역 크기
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                ret += 1
    
    return ret
                
                
        


n, m = map(int, input().rstrip().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))

# 빈 칸 리스트
location = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            location.append([i, j])
ans = 0
for selected in combinations(location, 3):
    ans = max(ans, bfs(selected))

print(ans)
    
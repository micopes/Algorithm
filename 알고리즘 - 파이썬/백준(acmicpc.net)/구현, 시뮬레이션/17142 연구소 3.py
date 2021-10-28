import sys
import copy
from collections import deque
from itertools import combinations
# input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(selected):
    visited = copy.deepcopy(graph)
    
    q = deque()
    
    unact_virus = set()
    # 벽 위치
    for i in range(n):
    	for j in range(n):
            # 벽 
            if visited[i][j] == 1:
                visited[i][j] = -1
            # Virus
            elif visited[i][j] == 2:
                visited[i][j] = 0
                unact_virus.add((i, j))
                
    # 바이러스의 초기 위치
    for x, y in selected:
        q.append([x, y])
        visited[x][y] = 1
        unact_virus.remove((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    
    time = 0
    for x, y in unact_virus:
        visited[x][y] = 1
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                return sys.maxsize
            else:
                time = max(time, visited[i][j])


    return time
    

n, m = map(int, input().rstrip().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))
    
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append([i, j])
        
time = sys.maxsize
for selected in combinations(virus, m):
    time = min(time, bfs(selected))

if time == sys.maxsize:
    print(-1)
else:
    # 처음에 1로 시작했기 때문에.
    print(time-1)
    

    
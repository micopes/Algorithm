import sys
from collections import deque
# input = sys.stdin.readline

n = int(input().rstrip())
graph = []

for i in range(n):
    temp = list(map(int, input().rstrip().split()))
    graph.append(temp)

r, c = -1, -1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            r, c = i, j
            break
        
size = 2
eat = 0
stage = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while True:
    q = deque()
    q.append([r, c, 0])
    
    fish = []
    visited = [[0 for j in range(n)] for i in range(n)]
    visited[r][c] = 1
    flag = 1e9
    
    while q:
        x, y, count = q.popleft()
        
        if count > flag:
            break
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if 0 < graph[nx][ny] < size:
                    q.append([nx, ny, count+1])
                    fish.append([nx, ny, count+1])
                    visited[nx][ny] = 1
                    flag = count
                
                if graph[nx][ny] == 0 or graph[nx][ny] == size:
                    q.append([nx, ny, count+1])
                    visited[nx][ny] = 1
        
    
    if len(fish) > 0:
        fish.sort()
        r, c, count = fish[0][0], fish[0][1], fish[0][2]
        stage += count
        graph[r][c] = 0
        eat += 1
        if eat == size:
            size += 1
            eat = 0
    else:
        break

print(stage)
    


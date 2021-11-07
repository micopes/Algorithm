import sys
# input = sys.stdin.readline
from collections import deque

def answer():
    ret = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    return -1
                elif ret < graph[i][j][k]:
                    ret = graph[i][j][k]
                
    return ret

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

graph = []

m, n, h = map(int, input().rstrip().split())
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().rstrip().split())))
    graph.append(tmp)

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append([i, j, k])
            
while q:
    x, y, z = q.popleft()
    
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
            graph[nx][ny][nz] = graph[x][y][z] + 1
            q.append([nx, ny, nz])

ans = answer()

if ans > 0:
    print(ans-1)
else:
    print(ans) # -1
    


    
            
            
            
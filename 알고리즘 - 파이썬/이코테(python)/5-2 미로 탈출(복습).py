import sys
# input = sys.stdin.readline
from collections import deque

n, m = map(int, input().rstrip().split())

graph = []
visited = [[0]*m for _ in range(n)] # [0][0] ~ [n-1][m-1]
for i in range(n):
    graph.append(list(input())) # string
    
q = deque()

q.append([0, 0])
visited[0][0] = 1 # 방문 : 1, 미방문 : 0
graph[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    k = q.popleft()
    x = k[0]
    y = k[1]
    if x == n-1 and y == m-1:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == '1':
                q.append([nx, ny])
                visited[nx][ny] = 1
                graph[nx][ny] = graph[x][y] + 1

print(graph[n-1][m-1])

    




    
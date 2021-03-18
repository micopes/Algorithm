import sys
from collections import deque
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [] # (0, 0) ~ (n-1, m-1)
visited = [[0]*m for _ in range(n)]

for i in range(n):
    string = input()
    graph.append(list(string)) # '0', '1'

q = deque()
q.append([0, 0, 1])
visited[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y, dist = q.popleft()
    if x == n-1 and y == m-1:
        print(dist)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and graph[nx][ny] == '1':
                q.append([nx, ny, dist+1])
                visited[nx][ny] = 1
    
        
        

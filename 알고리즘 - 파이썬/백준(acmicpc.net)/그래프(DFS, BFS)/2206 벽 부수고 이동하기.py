import sys
from collections import deque
# input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1 # 맨 마지막 0이 벽을 안부순 것, 1이 벽을 이미 부순 것
    q = deque()
    q.append([0, 0, 0])
    
    while q:
        x, y, w = q.popleft()
        
        if x == n-1 and y == m-1:
            return visited[x][y][w]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 막혀있고, 벽을 아직 안부순 경우
                if graph[nx][ny] == 1 and w == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append([nx, ny, 1])
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append([nx, ny, w])
    return -1
    

n, m = map(int, input().rstrip().split())

graph = []
for _ in range(n):
    string = input()
    graph.append(list(string))

for i in range(n):
    for j in range(m):
        graph[i][j] = int(graph[i][j])


print(bfs())
    

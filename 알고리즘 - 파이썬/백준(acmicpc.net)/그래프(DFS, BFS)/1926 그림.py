import sys
# input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def bfs(x, y):
    global cnt
    cnt += 1
    
    q = deque()
    q.append((x, y))
    visited[x][y] = cnt
    
    while q:
        temp = q.popleft()
        x = temp[0]
        y = temp[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = cnt
    

n, m = map(int, input().strip().split()) # 행 : n, 열 : m

visited = [[0 for _ in range(m)] for _ in range(n)]
graph = []
for i in range(n):
    temp = list(map(int, input().rstrip().split()))
    graph.append(temp)

cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)

print(cnt)
number_of_cnt = [0]*(cnt+1)
for i in range(n):
    for j in range(m):
        val = visited[i][j]    
        number_of_cnt[val] += 1

ans = 0
for i in range(1, cnt+1):
    if ans < number_of_cnt[i]:
        ans = number_of_cnt[i]

print(ans)
    
    
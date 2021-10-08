import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    visited[i][j] = cnt
    q = deque()
    q.append([i, j])
    
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            
            if 0 <= nr < m and 0 <= nc < n:
                if visited[nr][nc] == 0 and graph[nr][nc] == 1:
                    q.append([nr, nc])
                    visited[nr][nc] = cnt
        
    
    
# m : 행, n : 열
m, n, k = map(int, input().rstrip().split())

graph = [[1 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]

# 원래 1인 것들 0으로 채우고
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    # x와 m이 반대이므로 이를 주의.
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 0

cnt = 1
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            cnt += 1

ans_list = [0 for _ in range(cnt)]

for i in range(m):
    for j in range(n):
        temp = visited[i][j]
        ans_list[temp] += 1

ans_list.pop(0)
ans_list.sort()

print(cnt-1)
for k in ans_list:
    print(k, end = " ")
        
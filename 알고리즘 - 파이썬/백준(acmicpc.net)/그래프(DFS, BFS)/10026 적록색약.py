from collections import deque
import sys
# input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs1(x, y, count):
    cnt = 1
    visited1[x][y] = count
    
    q = deque()
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited1[nx][ny] == 0 and graph[x][y] == graph[nx][ny]:
                visited1[nx][ny] = visited1[x][y]
                q.append([nx, ny])
                
def bfs2(x, y, count):
    cnt = 1
    visited2[x][y] = count
    
    q = deque()
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited2[nx][ny] == 0 and (graph[x][y] == graph[nx][ny] or (graph[x][y] == 'G' and graph[nx][ny] == 'R') or (graph[x][y] == 'R' and graph[nx][ny] == 'G')):
                visited2[nx][ny] = visited2[x][y] 
                q.append([nx, ny])

# 위의 1, 2번으로 나누는 연결 요소의 개수 문제.
n = int(input().rstrip())
graph = []

for i in range(n):
    graph.append(list(input().rstrip()))

# 1. R, G, B
visited1 = [[0]*n for _ in range(n)]
cnt1 = 1

for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:
            bfs1(i, j, cnt1)
            cnt1 += 1
            
            
# 2. R-G, B
visited2 = [[0]*n for _ in range(n)]   
cnt2 = 1

for i in range(n):
    for j in range(n):
        if visited2[i][j] == 0:
            bfs2(i, j, cnt2)
            cnt2 += 1
            
            
print(cnt1-1, cnt2-1)

        
from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j, cnt):
    dq.append([i, j])
    c[i][j] = cnt
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 1 and c[nx][ny] == 0:
                    c[nx][ny] = cnt
                    dq.append([nx, ny])

def bfs2(num):
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 1 and c[nx][ny] != num:
                    return c2[x][y]-1
                if a[nx][ny] == 0 and c2[nx][ny] == 0:
                    c2[nx][ny] = c2[x][y] + 1
                    dq.append([nx, ny])
                    
                

n = int(input().strip())
a = [list(map(int, input().strip().split())) for _ in range(n)]
c = [[0]*n for _ in range(n)]

dq = deque()
cnt = 1
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and c[i][j] == 0:
            bfs(i, j, cnt)
            cnt += 1

result = 10000
for k in range(1, cnt):
    dq = deque()
    c2 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if c[i][j] == k and a[i][j] == 1:
                dq.append([i, j])
                c2[i][j] = 1
    ans = bfs2(k)
    result = min(ans, result)
print(result)
                
            


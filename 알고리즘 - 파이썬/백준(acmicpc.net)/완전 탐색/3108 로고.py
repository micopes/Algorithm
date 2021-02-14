import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 2000 and 0 <= ny <= 2000:
                if a[nx][ny] == 1 and c[nx][ny] == 0:
                    q.append([nx, ny])
                    c[nx][ny] = 1
        

n = int(input().rstrip())
a = [[0]*2001 for _ in range(2001)]
c = [[0]*2001 for _ in range(2001)]
start = []
for i in range(n):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    x1 = (x1+500)*2
    y1 = (y1+500)*2
    x2 = (x2+500)*2
    y2 = (y2+500)*2
    start.append([x1, y1])
    for i in range(x1, x2+1):
        if i == x1 or i == x2:
            for j in range(y1, y2+1):
                a[i][j] = 1
        else:
            a[i][y1] = 1
            a[i][y2] = 1
    

ans = 0
q = deque()
for i in range(len(start)):
    x, y = start[i]
    if c[x][y] == 0:
        bfs(x, y)
        ans += 1

if c[1000][1000] == 1:
    ans -= 1

print(ans)
    
    
    
    
    
    
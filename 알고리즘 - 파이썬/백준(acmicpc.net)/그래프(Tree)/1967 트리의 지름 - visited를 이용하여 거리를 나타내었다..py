import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, mode):
    dq = deque()
    dq.append(start)
    c = [-1 for _ in range(10001)]
    c[start] = 0
    while dq:
        x = dq.popleft()
        for dist, n in data[x]:
            if c[n] == -1:
                c[n] = c[x] + dist
                dq.append(n)
    
    if mode == 1:
        return c.index(max(c))
    else:
        return max(c)
    

n = int(input().strip())

data = [[] for _ in range(10001)] # 1 ~ 10000

for i in range(n-1):
    nx, ny, dist = map(int, input().strip().split())
    data[nx].append([dist, ny])
    data[ny].append([dist, nx])
    
print(bfs(bfs(1, 1), 2))
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, mode):
    q = deque()
    q.append(x)
    c = [-1 for _ in range(n+1)]
    c[x] = 0
    while q:
        nx = q.popleft()
        for ny, dist in data[nx]:
            if c[ny] == -1:
                c[ny] = c[nx] + dist
                q.append(ny)
    
    if mode == 1:
        return c.index(max(c))
    else:
        return max(c)
    
# 1 ~ n으로 범위를 지정할 것.
n = int(input().strip())
data = [[] for _ in range(n+1)]

for i in range(n):
    _list = list(map(int, input().strip().split()))
    x = _list[0]
    for j in range(1, len(_list), 2):
        y = _list[j]
        if y == -1:
            break
        dist = _list[j+1]
        data[x].append([y, dist])
        data[y].append([x, dist])

print(bfs(bfs(1, 1), 2))

import sys
# input = sys.stdin.readline
from collections import deque

n, k = map(int, input().strip().split())
visited = [0 for _ in range(100001)]
dist = [0 for _ in range(100001)]

dq = deque()
dq.append(n)
while dq:
    x = dq.popleft()
    if x == k:
        break
    for i in [x-1, x+1, x*2]: # x*2를 먼저해주면 안된다.
        if i >= 0 and i <= 100000 and visited[i] == 0:
            visited[i] = 1
            dist[i] = dist[x] + 1
            dq.append(i)

print(dist[k])
        


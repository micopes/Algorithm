import sys
from collections import deque
input = sys.stdin.readline

INF = sys.maxsize
n = int(input().rstrip())

depth = [INF for _ in range(n+1)]
depth[1] = 1

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
while q:
    x = q.popleft()
    for i in graph[x]:
        if depth[i] == INF:
            depth[i] = x
            q.append(i)

for i in range(2, n+1):
    print(depth[i])
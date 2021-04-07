import sys
from collections import deque
# input = sys.stdin.readline
_INF = -sys.maxsize

def bfs(v):
    visited = [0 for _ in range(n+1)]
    visited[v] = 1
    
    q = deque()
    q.append(v)
    while q:
        x = q.popleft()
        if x == n:
            return True
        for edge in graph:
            cur = edge[0]
            next_v = edge[1]
            if cur == x and visited[next_v] == 0:
                q.append(next_v)
                visited[next_v] = 1
    return False

def bf(start):
    dist[start] = 0
    
    for i in range(n):
        for edge in graph:
            cur = edge[0]
            next_v = edge[1]
            d = edge[2]
            if dist[cur] != _INF and dist[next_v] < dist[cur] + d:
                dist[next_v] = dist[cur] + d
                path[next_v] = cur
                if i == n-1:
                    if bfs(next_v) == True:
                        return True
    return False

n, m = map(int, input().rstrip().split())

graph = []
dist = [_INF]*(n+1)
path = [0 for _ in range(n+1)]

for i in range(m):
    u, v, w = map(int, input().rstrip().split())
    graph.append((u, v, w))

cycle = bf(1)
if cycle == True or dist[n] == _INF:
    print(-1)
else:
    ans = []
    ans.append(n)
    val = n
    while val != 1:
        k = path[val]
        ans.append(k)
        val = k
    ans = ans[::-1]
    for i in ans:
        print(i, end = " ")
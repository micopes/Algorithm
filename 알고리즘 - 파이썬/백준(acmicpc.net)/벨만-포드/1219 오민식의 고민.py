import sys
from collections import deque
input = sys.stdin.readline
INF = -sys.maxsize

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    
    while q:
        x = q.popleft()
        if x == end:
            return True
        for edge in graph:
            cur = edge[0]
            next_v = edge[1]
            if cur == x and visited[next_v] == 0:
                visited[next_v] = 1
                q.append(next_v)
    return False

def bf(start):
    for i in range(N):
        for edge in graph:
            cur = edge[0]
            next_v = edge[1]
            cost = edge[2]
            if dist[cur] != INF and dist[next_v] < dist[cur] + cost + earn[next_v]:
                dist[next_v] = dist[cur] + cost + earn[next_v]
                
                if N-1 == i:
                    ret = bfs(next_v)
                    if ret == True:
                        return True
    return False
    

N, start, end, M = map(int, input().rstrip().split())

graph = []
dist = [INF]*(N+1)
visited = [0]*(N+1)
earn = []

for i in range(M):
    x, y, d = map(int, input().rstrip().split())
    graph.append([x, y, -d])
    
earn = list(map(int, input().rstrip().split()))
dist[start] = earn[start]

cycle = bf(start)
if dist[end] == INF:
    print("gg")
elif cycle == True:
    print("Gee")
else:
    print(dist[end])

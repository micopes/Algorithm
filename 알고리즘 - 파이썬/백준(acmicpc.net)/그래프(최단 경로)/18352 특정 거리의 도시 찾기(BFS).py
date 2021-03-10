from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().rstrip().split())

graph = [[] for _ in range(N+1)] # 1 ~ N
visited = [0 for _ in range(N+1)]
q = deque()

for i in range(M):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)

ans = []

q.append([X, 0])
visited[X] = 1

while q:
    x, dist = q.popleft()
    
    if dist == K:
        ans.append(x)
        continue

    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = 1
            q.append([i, dist+1])
            
if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)

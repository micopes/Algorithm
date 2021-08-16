import sys
from collections import deque
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    print(x, end = " ")
    for i in graph[x]:
        indegree[i] -= 1
        
        if indegree[i] == 0:
            q.append(i)


import sys
# input = sys.stdin.readline

from collections import deque

V, E = map(int, input().rstrip().split())

indegree = [0 for _ in range(V+1)]
graph = [[] for _ in range(V+1)]

for i in range(E):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, V+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        x = q.popleft()
        result.append(x)
        
        for i in graph[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
        
    for i in result:
        print(i, end = " ")

topology_sort()
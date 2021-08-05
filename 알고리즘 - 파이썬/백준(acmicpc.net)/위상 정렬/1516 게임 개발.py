import sys
# input = sys.stdin.readline

from collections import deque

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

cost = [0 for _ in range(n+1)]

for i in range(1, n+1):
    li = list(map(int, input().rstrip().split()))
    cost[i] = li[0]
    
    
    for j in range(1, len(li)-1):
        graph[li[j]].append(i)
        indegree[i] += 1
        
def topology_sort():
    result = [0 for _ in range(n+1)]
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = cost[i]
            
    while q:
        x = q.popleft()
        for i in graph[x]:
            result[i] = max(result[i], result[x] + cost[i])
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, n+1):
        print(result[i])
        
topology_sort()
        
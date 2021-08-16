import sys
# input = sys.stdin.readline
from collections import deque
import copy
 
T = int(input().rstrip())
 
 
 
for _ in range(T):
    n, k = map(int, input().rstrip().split())
 
    cost = []
    indegree = [0 for _ in range(n+1)] # 1 ~ N+1
    graph = [[] for _ in range(n+1)]
 
 
    cost = list(map(int, input().rstrip().split())) # 각 건물을 짓는데 걸리는 시간
    cost2 = [0]
    for i in cost: # 1 ~ n이므로 0번째에 추가.
        cost2.append(i)
 
    for i in range(k): # 건설 순서
        a, b = map(int, input().rstrip().split())
        indegree[b] += 1
        graph[a].append(b)
 
 
    result = copy.deepcopy(cost2)
    q = deque()
 
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
 
    while q:
        x = q.popleft()
        for i in graph[x]:
            result[i] = max(result[i], result[x] + cost2[i])
            indegree[i] -= 1
 
            if indegree[i] == 0:
                q.append(i)
 
    target = int(input().rstrip())# 건물 W를 건설하는데 드는 최소 시간
    print(result[target])
 
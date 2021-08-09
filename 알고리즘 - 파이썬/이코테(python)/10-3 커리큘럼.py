from collections import deque
import copy # deep copy를 위해
import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
cost = [0 for _ in range(n+1)] # 해당 과목의 비용

for i in range(1, n+1):
    li = list(map(int, input().rstrip().split()))
    cost[i] = li[0]
    
    for x in li[1:-1]:
        graph[x].append(i)
        indegree[i] += 1

def topology_sort():
    result = copy.deepcopy(cost)
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        x = q.popleft()
        
        for i in graph[x]:
            result[i] = max(result[x] + cost[i], result[i]) # x를 거치는 것과 기존의 것 비교. 위상정렬으로 인해 계속 커진다.
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, n+1):
        print(result[i])

topology_sort()
            
        
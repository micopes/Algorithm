import sys
# input = sys.stdin.readline

from collections import deque

N, M = map(int, input().rstrip().split())# 가수, 보조 PD
indegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    li = list(map(int, input().rstrip().split()))
    for i in range(1, len(li)-1):
        a = li[i]
        b = li[i+1]
        graph[a].append(b)
        indegree[b] += 1


def topology_sort():
    result = [] # 최종적으로 result == N인 경우에는 0을 출력하면 된다.
    q = deque()
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        x = q.popleft()
        result.append(x)
        
        for i in graph[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    if len(result) != N:
        print(0)
    else:
        for i in result:
            print(i)

topology_sort()
            
        
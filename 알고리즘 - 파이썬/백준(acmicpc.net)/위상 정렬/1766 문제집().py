import sys
import heapq
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

indegree = [0 for _ in range(n+1)] # 1 ~ n
graph = [[] for _ in range(n+1)] # 리스트
heap = []
result = []

for i in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    indegree[y] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    x = heapq.heappop(heap)
    result.append(x)
    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)

for i in result:
    print(i, end = " ")
    
        


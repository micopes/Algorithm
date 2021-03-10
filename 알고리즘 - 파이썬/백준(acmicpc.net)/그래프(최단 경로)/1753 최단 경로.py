import heapq
import sys
# input = sys.stdin.readline

def Dijkstra(start):
    dp[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    
    while heap:
        w, v = heapq.heappop(heap)
        
        if w > dp[v]:
            continue
        
        for nextW, toV in graph[v]:
            startToNext = w + nextW
            if startToNext < dp[toV]:
                dp[toV] = startToNext
                heapq.heappush(heap, [startToNext, toV])
        
V, E = map(int, input().rstrip().split())
K = int(input().rstrip()) # 시작 정점
INF = sys.maxsize
graph = [[] for _ in range(V+1)] # 1 ~ V
dp = [INF for _ in range(V+1)] # 시작점에서의 비용(가중치)

for i in range(E):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append([w, v]) # 이후 heapq.heappop(heap) 시에 w부터 나오기 때문에.

Dijkstra(K)

for i in range(1, V+1):
    print("INF" if dp[i] == INF else dp[i])

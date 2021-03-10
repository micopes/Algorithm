import sys
import heapq
# input = sys.stdin.readline

def Dijkstra(start):
    heap = []
    dp[start] = 0
    heapq.heappush(heap, [0, start])
    
    while heap:
        w, v = heapq.heappop(heap)
        
        if w > dp[v]:
            continue
    
        for nextW, toV in graph[v]:
            startToNext = nextW + w
            if startToNext < dp[toV]:
                dp[toV] = startToNext
                heapq.heappush(heap, [startToNext, toV])
                
    
N, M, K, X = map(int, input().rstrip().split())
INF = sys.maxsize
graph = [[] for _ in range(N+1)]
dp = [INF for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().rstrip().split())
    graph[x].append([1, y])

Dijkstra(X)

ans = []
for i in range(1, N+1):
    if dp[i] == K:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    for x in ans:
        print(x)
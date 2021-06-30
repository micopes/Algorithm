import sys
import heapq
# input = sys.stdin.readline

INF = sys.maxsize

n, m, c = map(int, input().rstrip().split())
dist = [INF for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y, w = map(int, input().rstrip().split())
    graph[x].append((y, w))

def dijkstra(start):
    heap = []
    dist[start] = 0
    heapq.heappush(heap, (0, start)) # key = lambda x : 안쓰기 위해서 가중치를 [0]에 두었다.
    
    while heap:
        k = heapq.heappop(heap)
        d = k[0]
        n = k[1]
        for temp in graph[n]:
            temp[0] # 연결된 node
            temp[1] # 연결된 node와의 거리
            cost = temp[1] + d
            if cost < dist[temp[0]]:
                heapq.heappush(heap, (cost, temp[0]))
                dist[temp[0]] = cost

dijkstra(c)

cnt = 0
max_dist = 0

for i in range(1, n+1):
    if dist[i] != INF:
        cnt += 1
        max_dist = max(max_dist, dist[i])

print(cnt-1, max_dist)


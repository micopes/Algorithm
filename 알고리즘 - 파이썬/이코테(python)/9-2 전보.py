import sys
import heapq
# input = sys.stdin.readline

INF = sys.maxsize
n, m, c = map(int, input().rstrip().split())

graph = [[] for _ in range(n+1)] # 1 ~ n
dist = [INF for _ in range(n+1)]

for i in range(m):
    x, y, w = map(int, input().rstrip().split())
    graph[x].append((y, w))

# 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간

# C에서 도달할 수 있는 도시 모두 구하고,
# 구한 도시들 중 가장 거리가 먼 것을 출력하면 된다.
# 개수, 가장 먼 것 출력

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start)) # (걸리는 시간, 현재 위치)
    dist[start] = 0 # 자기 자신은 0으로 초기화
    while heap:
        x = heapq.heappop(heap)
        d = x[0]
        node = x[1]
        if d < dist[node]: # 이전에 구한 것이 이미 더 최단거리일 경우
            continue
        for k in graph[node]: # k[0] : node, k[1] : distance
            cost = d + k[1]
            if cost < dist[k[0]]:
                heapq.heappush(heap, (k[1], d + k[0]))
                dist[k[0]] = cost

dijkstra(c)
cnt = 0
ans = 0
for d in dist:
    if d != INF:
        cnt += 1
        ans = max(d, ans)

print(cnt-1, ans) # 시작 노드는 제외
    
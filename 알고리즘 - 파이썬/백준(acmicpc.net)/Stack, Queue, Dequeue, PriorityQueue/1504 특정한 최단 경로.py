import sys
import heapq
input = sys.stdin.readline

# node간 거리가 1이 아니라 가중치가 있기 때문에
# 그냥 dfs, bfs로 풀 수 없다 -> pq 사용!
INF = sys.maxsize
def dijkstra(start):
    dist = [INF for _ in range(801)]
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [dist[start], start])
    while heap:
        x = heapq.heappop(heap)[1]
        for v, d in edge[x]:
            if dist[v] > dist[x] + d:
                dist[v] = dist[x] + d
                heapq.heappush(heap, [dist[v], v])
    return dist

N, E = map(int, input().rstrip().split())
edge = [[] for _ in range(801)]

for i in range(E):
    x, y, d = map(int, input().rstrip().split())
    edge[x].append([y, d])
    edge[y].append([x, d])

v1, v2 = map(int, input().rstrip().split())

# 경로는 2가지
# 1. 1 -> v1 -> v2 -> N
# 2. 1 -> v2 -> v1 -> N

# 거리에 관한 리스트를 리턴받아서 사용한다.
from_1 = dijkstra(1)
from_v1 = dijkstra(v1)
from_v2 = dijkstra(v2)

path1 = from_1[v1] + from_v1[v2] + from_v2[N]
path2 = from_1[v2] + from_v2[v1] + from_v1[N]

ans = min(path1, path2)
if ans < INF:
    print(ans)
else:
    print(-1)



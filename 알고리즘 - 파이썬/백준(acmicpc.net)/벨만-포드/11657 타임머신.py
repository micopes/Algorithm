import sys
# input = sys.stdin.readline
INF = sys.maxsize

def bf(start):
    dist[start] = 0
    
    for i in range(v):
        for edge in graph:
            cur = edge[0]
            next_v = edge[1]
            cost = edge[2]
            
            # dist[cur] != INF를 넣어주는 이유는 이 조건이 있어야
            # 시작지점부터 연결된 노드를 찾을 수 있기 때문에.
            if dist[cur] != INF and dist[next_v] > dist[cur] + cost:
                dist[next_v] = dist[cur] + cost
                if i == v-1:
                    return True
    return False


v, e = map(int, input().rstrip().split())
graph = []
dist = [INF]*(v+1)

for i in range(e):
    x, y, d = map(int, input().rstrip().split())
    graph.append([x, y, d])

negative_cycle = bf(1)
    
if negative_cycle == True:
    print(-1)
else:
    for i in range(2, v+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
    
import sys
input = sys.stdin.readline
INF = sys.maxsize

def bf(start):
    dist[start] = 0
    
    for i in range(v):
        for j in range(e):
            cur = graph[j][0]
            next_v = graph[j][1]
            cost = graph[j][2]
            
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
    
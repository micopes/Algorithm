import sys
input = sys.stdin.readline
INF = sys.maxsize

def bf(start):
    # 시작 노드에 대해서 초기화
    dist[start] = 0
    # 전체 v번 반복(vertex)
    for i in range(v):
        # 매 반복마다 모든 간선(edge) 확인
        for j in range(e):
            cur = graph[j][0]
            next_v = graph[j][1]
            cost = graph[j][2]
            
            if dist[cur] != INF and dist[next_v] > dist[cur] + cost:
                dist[next_v]
                if i == n-1:
                    return True
    return False

v, e = map(int, input().rstrip().split())
graph = []
dist = [INF]*(v+1)

for i in range(v):
    x, y, d = map(int, input().rstrip().split())
    graph.append([x, y, d])

negative_cycle = bf(1)

# 출력
if negative_cycle:
    print(-1)
else:
    for i in range(2, v+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
        
import sys
input = sys.stdin.readline

V, E = map(int, input().rstrip().split())

INF = sys.maxsize
graph = [[INF]*(V+1) for _ in range(V+1)]

for i in range(E):
    a, b, dist = map(int, input().rstrip().split())
    graph[a][b] = dist

for i in range(1, V+1):
    graph[i][i] = INF

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = INF
for i in range(1, V+1):
    if graph[i][i] < ans:
        ans = graph[i][i]

if ans == INF:
    print(-1)
else:
    print(ans)
    
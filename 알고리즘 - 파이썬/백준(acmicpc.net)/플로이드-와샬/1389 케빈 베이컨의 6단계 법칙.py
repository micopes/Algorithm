import sys
input = sys.stdin.readline

# 모두와의 최단경로가 필요하기 때문에 플로이드 와샬을 적용.

INF = sys.maxsize

n, m = map(int, input().rstrip().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x][y] = 1
    graph[y][x] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = [0]*(n+1)
result[0] = INF

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] != INF:
            result[i] += graph[i][j]

print(result.index(min(result)))



                                   
                                   
    
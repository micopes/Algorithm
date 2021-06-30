import sys
# input = sys.stdin.readline

INF = sys.maxsize

n, m = map(int, input().rstrip().split()) # n, m이 400이하인 100이므로 O(n^3)에서 사용가능한 플로이드-와샬 알고리즘 적용
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().rstrip().split()) # 1 -> K -> X

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            



# 도달할 수 없는 경우
if graph[1][K] >= INF or graph[K][X] >= INF:
    print(-1)
else:
    ans = graph[1][K] + graph[K][X]
    print(ans)


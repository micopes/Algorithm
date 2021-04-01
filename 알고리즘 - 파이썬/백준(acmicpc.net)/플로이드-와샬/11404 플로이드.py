import sys
input = sys.stdin.readline

# 도시의 개수
n = int(input().rstrip())

# 버스의 개수
m = int(input().rstrip())

INF = sys.maxsize

graph = [[INF]*101 for _ in range(101)]

for i in range(m):
    x, y, dist = map(int, input().rstrip().split())
    # x->y로 가는 버스 중 더 빠른 것이 있을 수도 있다.
    graph[x][y] = min(graph[x][y], dist)

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()

    




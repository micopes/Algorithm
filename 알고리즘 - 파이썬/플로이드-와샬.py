import sys
# input = sys.stdin.readline

INF = sys.maxsize

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0 # 자기 자신으로 가는 것은 1로 초기화

    
for _ in range(m):
    a, b, w = map(int, input().rstrip().split())
    graph[a][b] = w # 단방향 그래프

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("Infinity")
        else:
            print(graph[i][j], end = " ")
    
    print()


            



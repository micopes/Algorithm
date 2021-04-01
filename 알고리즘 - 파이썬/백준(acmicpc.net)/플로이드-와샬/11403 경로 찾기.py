import sys
# input = sys.stdin.readline

INF = sys.maxsize

n = int(input().rstrip())

graph = []
for i in range(n):
    temp = list(map(int, input().rstrip().split()))
    graph.append(temp)
    
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF
            

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()


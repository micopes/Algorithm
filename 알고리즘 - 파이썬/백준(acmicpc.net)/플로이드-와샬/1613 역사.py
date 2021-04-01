import sys
# input = sys.stdin.readline

# 전체에 대해 전후 관계를 구해야 하므로, 모든 경우를 고려하면 된다.

n, k = map(int, input().rstrip().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(k):
    x, y = map(int, input().rstrip().split())
    graph[x][y] = -1
    graph[y][x] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] == -1 and graph[k][j] == -1:
                graph[i][j] = -1
            elif graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

# 전후 관계를 알고 싶은 쌍의 수
s = int(input().rstrip())
for i in range(s):
    x, y = map(int, input().rstrip().split())
    print(graph[x][y])
    
    




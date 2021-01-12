import sys
input = sys.stdin.readline

def dfs(graph, k, isVisited):
    isVisited[k] = True
    
    for i in graph[k]:
        if isVisited[i] == 0:
            dfs(graph, i, isVisited)

graph = [[] for _ in range(1001)]
isVisited = [0 for _ in range(1001)]

n, m = map(int, input().split())
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, n+1): # 1 ~ N
    if isVisited[i] == 0:
        dfs(graph, i, isVisited)
        count += 1

print(count)
    
    

    
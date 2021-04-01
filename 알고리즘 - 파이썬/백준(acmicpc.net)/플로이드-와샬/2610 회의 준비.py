import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().rstrip())
m = int(input().rstrip())

INF = sys.maxsize
graph = [[INF]*(n+1) for _ in range(n+1)]
parent = [i for i in range(n+1)]

def find(target):
    if target == parent[target]:
        return target
    target = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x][y] = 1
    graph[y][x] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n+1):
    for j in range(n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
            
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if graph[i][j] >= 1:
            union(i, j)
            
community = set(parent)
community_list = []

for i in community:
    temp = sys.maxsize  
    tempIndex = -1
    for j in range(1, len(parent)):
        if parent[j] == i and temp > max(graph[j]):
            temp = max(graph[j])
            tempIndex = j
    community_list.append(tempIndex)

print(len(community_list)-1)
community_list.sort()
for i in range(1, len(community_list)):
    print(community_list[i])

            
            
            
    
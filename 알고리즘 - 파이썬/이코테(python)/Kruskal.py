import sys
# input = sys.stdin.readline

def find(n):
    if parent[n] == n:
        return n
    
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return a

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return 0

V, E = map(int, input().rstrip().split())
parent = [i for i in range(V+1)]
edge = []

for i in range(E):
    a, b, w = map(int, input().rstrip().split())
    edge.append((a, b, w))
    
edge.sort(key = lambda x : x[2])

cnt = 0
cost = 0

for i in range(E):
    a = edge[i][0]
    b = edge[i][1]
    if union(a, b) == 0:
        cnt += 1
        cost += edge[i][2]
    
    if cnt == V-1:
        break

print(cost)
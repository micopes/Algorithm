import sys
input = sys.stdin.readline

def find(n):
    if n == parent[n]:
        return n
    
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return a
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return 0
    

n, m = map(int, input().rstrip().split())
edge = []

for i in range(m):
    a, b, dist = map(int, input().rstrip().split())
    edge.append([a, b, dist])

edge.sort(key = lambda x : x[2])

cnt = 0
cost = 0 # ans
parent = [i for i in range(n+1)]
for i in range(m):
    a = edge[i][0]
    b = edge[i][1]
    dist = edge[i][2]
    if union(a, b) == 0:
        cnt += 1
        cost += dist
    
    if cnt == n-2:
        break

print(cost)
        
        
    
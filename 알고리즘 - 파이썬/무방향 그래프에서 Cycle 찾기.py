import sys
# input = sys.stdin.readline

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
    
    if a < b:
        parent[b] = a
    else:
        parnet[a] = b
    
    return 0


V, E = map(int, input().rstrip().split())
edge = []

parent = [i for i in range(V+1)]

for i in range(E):
    a, b, w = map(int, input().rstrip().split())
    edge.append((a, b, w))

cycle = False # Cycle 발생 여부

for i in range(E):
    a = edge[i][0]
    b = edge[i][1]
    if union(a, b) != 0: # 이미 연결되어 있는데 a, b가 연결되어 있으면 Cycle
        cycle = True
        break

if cycle == True:
    print("Cycle")
else:
    print("Not Cycle")
        
        

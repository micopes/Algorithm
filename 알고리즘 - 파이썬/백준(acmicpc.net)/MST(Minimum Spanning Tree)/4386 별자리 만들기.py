import sys
import math
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
        return True
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return False
        

n = int(input().rstrip())
node = []
for i in range(n):
    x, y = map(float, input().rstrip().split())
    node.append([x, y])
    
edge = []
for i in range(n-1):
    for j in range(i+1, n):
        weight = round(math.sqrt((node[i][0] - node[j][0])**2 + (node[i][1] - node[j][1])**2), 2)
        edge.append([i, j, weight])

edge.sort(key = lambda x : x[2])

cnt = 0
cost = 0
parent = [i for i in range(n+1)] # 1 ~ n
for i in range(len(edge)):
    if union(edge[i][0], edge[i][1]) == False:
        cnt += 1
        cost += edge[i][2]
    if cnt == n-1:
        break

print(cost)
        
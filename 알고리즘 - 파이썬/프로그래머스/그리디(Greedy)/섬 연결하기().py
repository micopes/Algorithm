# MST

def find(parent, n):
    if parent[n] == n:
        return n
    
    parent[n] = find(parent, parent[n])
    return parent[n]
    
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a == b:
        return a
    
    if a < b:
        parent[a] = b
    else:
        parent[b] = a
    return 0

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    edge = []
    
    for x in costs:
        a, b, w = x
        edge.append([a, b, w])
    
    edge.sort(key = lambda x : x[2])        
    
    cnt = 0
    cost = 0
    
    for x in edge:
        a = x[0]
        b = x[1]
        if union(parent, a, b) == 0:
            cnt += 1
            cost += x[2]
            print(a, b, x[2])
        
        if cnt == n-1:
            break
    
    return cost
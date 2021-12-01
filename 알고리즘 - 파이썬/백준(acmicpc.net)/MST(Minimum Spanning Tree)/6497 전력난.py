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
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b
        
    return -1
    

while True:
    m, n = map(int, input().rstrip().split())
    
    if m == 0 and n == 0:
        break
    
    parent = [i for i in range(m)]
    edge = []
    ans = 0
    for i in range(n):
        a, b, w = map(int, input().rstrip().split())
        edge.append((a, b, w))
        ans += w
    
    edge.sort(key = lambda x : x[2])
    
    cnt = 0
    for x in edge:
        a, b, w = x
        
        if union(a, b) == -1:
            ans -= w
            cnt += 1
        if cnt == m-1:
            break
    print(ans)
    
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
        parent[a] = b
        
    return 0
    


n, m = map(int, input().rstrip().split())

edge = []
parent = [i for i in range(n+1)]
cnt = 0
ans = 0

for i in range(m):
    a, b, w = map(int, input().rstrip().split())
    edge.append([a, b, w])

edge.sort(key = lambda x : x[2])

for x in edge:
    a = x[0]
    b = x[1]
    w = x[2]
    if union(a, b) == 0: # 연결이 되어 있지 않은 경우
        ans += w
        cnt += 1
    if cnt == n-2:
        break

print(ans)
        
        
    
    


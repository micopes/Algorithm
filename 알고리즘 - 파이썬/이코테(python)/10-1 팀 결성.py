import sys
# input = sys.stdin.readline

def find(n):
    if n == parent[n]:
        return n
    
    n = find(parent[n])
    return n

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return 0
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
    return a
        


N, M = map(int, input().rstrip().split())

parent = [i for i in range(N+1)] # N+1개 존재. 0 ~ N번까지.

# 0 : 팀 합치기, 1 : 같은 팀 여부 확인
for i in range(M):
    command, x, y = map(int, input().rstrip().split())
    if command == 0: # 팀 합치기
        union(x, y)
    else: # 같은 팀 여부 확인
        if find(x) == find(y):
            print("YES")
        else:
            print("NO")
            
        
    
    
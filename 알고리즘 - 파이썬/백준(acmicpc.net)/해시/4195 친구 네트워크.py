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
    
    if parent[a] != parent[b]:
        parent[b] = a
        number[a] += number[b]

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    parent = {}
    number = {}
    
    for _ in range(n):
        x, y = input().rstrip().split()
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union(x, y)
        
        # number[find(a)] 도 가능. 계속 올라가다가 그룹의 수가 
        # parent[n]에 나타남.
        
        print(number[find(y)])
        
        
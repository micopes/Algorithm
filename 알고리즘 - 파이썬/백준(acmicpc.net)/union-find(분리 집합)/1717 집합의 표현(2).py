import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(n):
    if n == parent[n]: # 부모가 자기 자신인 경우
        return n;
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().rstrip().split())
parent = [i for i in range(n+1)]
for i in range(m):
    command, a, b = map(int, input().rstrip().split())
    if command == 0:
        union(a, b)
    if command == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
        
        
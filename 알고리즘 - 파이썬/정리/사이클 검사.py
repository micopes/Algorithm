# 원래 부모가 같았던 경우에 사이클이 만들어진다. 20040 사이클 게임 참고.
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
        return 0
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
    return 1

n, m = map(int, input().rstrip().split())
parent = [i for i in range(n)]

ans = 0
for i in range(m):
    a, b = map(int, input().rstrip().split())
    
    # 원래 부모가 같았던 경우
    if union(a, b) == 0:
        ans = i+1
        break

print(ans)
        
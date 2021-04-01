import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().rstrip().split())
parent = [i for i in range(n+1)]

def find(target):
    if target == parent[target]:
        return target
    
    parent[target] = find(parent[target])
    return parent[target]
  

def union(a, b):
    a = find(a)
    b = find(b)
    
    # 낮은 수로 통일
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    command, a, b = map(int, input().rstrip().split())
    # 합친다.
    if command == 0:
        union(a, b)
    # 같은 집합에 포함되어 있는지를 확인하는 연산
    elif command == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
        
        
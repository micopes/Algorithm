import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6) # recursionlimit 사용하면 메모리 초과 발생

def find(n):
    if n == parent[n]:
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b    
    else:
        ''' 
        이미 경로가 있음. 
        트리는 두 정점 간의 경로가 2개 이상이 되면 안되므로 트리가 아닌 것으로 처리.
        '''
        parent[a] = 0
        parent[b] = 0
    
def output(idx, n):
    if n == 0:
        print("Case %d: No trees." % idx)
    elif n == 1:
        print("Case %d: There is one tree." % idx)
    else:
        print("Case %d: A forest of %d trees." %(idx, n))

idx = 1
while True:
    n, m = map(int, input().rstrip().split())
    parent = [i for i in range(n+1)]
    if n == m == 0:
        break
    
    for i in range(m):
        a, b = map(int, input().rstrip().split())
        union(a, b)
    
    root = set(find(i) for i in parent)
    output(idx, len(root)-1) # 0은 제외
    idx += 1
    
    
        
    
    
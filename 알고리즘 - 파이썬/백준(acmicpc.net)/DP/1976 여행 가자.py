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
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

# 도시의 수 n
n = int(input().rstrip())
# 여행 계획에 속한 도시들의 수 m
m = int(input().rstrip())

parent = [i for i in range(n+1)]

for i in range(1, n+1):
    conn = list(map(int, input().rstrip().split()))
    for j in range(len(conn)):
        if conn[j] == 1:
            union(i, j+1)

conn = list(map(int, input().rstrip().split()))
ans = True
for i in range(1, len(conn)):
    if parent[conn[i]] != parent[conn[i-1]]:
        ans = False
        break
    

if ans == True:
    print("YES")
else:
    print("NO")
        
    


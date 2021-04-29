import sys
input = sys.stdin.readline

def find(n):
    if parent[n] == n:
        return n
    
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return a
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return 0

n = int(input().rstrip())
m = int(input().rstrip())
edge = []
for i in range(m):
    a, b, d = map(int, input().rstrip().split())
    if a == b: # 자기 자신으로 오는 것은 제거
        continue
    edge.append([a, b, d])

edge.sort(key = lambda x : x[2])

cnt = 0
cost = 0
parent = [i for i in range(n+1)]

for i in range(m):
    if union(edge[i][0], edge[i][1]) == 0: # 이제 연결한 경우(원래 연결되어 있지 않음)
	    cost += edge[i][2]
	    cnt += 1
    
    if cnt == n-1:
        break
print(cost)

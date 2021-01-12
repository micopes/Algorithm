from collections import deque

def dfs(data, v, isVisited):
    isVisited[v] = True
    print(v, end = " ")
    
    for i in data[v]:
        if not isVisited[i]:
            dfs(data, i, isVisited)
            
data = [[] for _ in range(1001)]
isVisited = [0 for _ in range(1001)]

n, m, v = map(int, input().split())

for i in range(m):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

for i in range(1, n+1):
    data[i].sort()

dfs(data, v, isVisited)
print()

isVisited = [0 for _ in range(1001)]

dq = deque()
dq.append(v)
result = [v]
isVisited[v] = 1
while len(dq) != 0:
    k = dq.popleft()
    for i in range(1, n+1):
        if isVisited[i] == 0 and k in data[i]:
            dq.append(i)
            result.append(i)
            isVisited[i] = 1

for i in range(len(result)):
    print(result[i], end = " ")
    
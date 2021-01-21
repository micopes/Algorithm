import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
data = [[] for _ in range(100001)]
visited = [0 for _ in range(100001)]

for i in range(n-1):
    x, y = map(int, input().strip().split())
    data[x].append(y)
    data[y].append(x)

dq = deque()
dq.append(1)
visited[1] = 1

while dq:
    x = dq.popleft()
    for i in range(len(data[x])):
        k = data[x][i]
        if visited[k] == 0:
            dq.append(k)
            visited[k] = x

for i in range(2, n+1):
    print(visited[i])
        


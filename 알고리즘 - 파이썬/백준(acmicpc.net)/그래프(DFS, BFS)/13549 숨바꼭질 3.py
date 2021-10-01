import sys
from collections import deque
# input = sys.stdin.readline

visited = [-1 for _ in range(100001)]

n, k = map(int, input().rstrip().split())

q = deque()

q.append([n, 0])
visited[n] = 0

while q:
    x = q.popleft()
    loc = x[0]
    count = x[1]
    
    if loc == k:
        print(count)
        break
    
    temp = x[0]
    if 0 <= 2*loc <= 100000 and visited[2*loc] == -1:
        q.append([loc*2, count])
        visited[2*loc] = count
    if 0 <= loc-1 <= 100000 and visited[loc-1] == -1:
        q.append([loc-1, count+1])
        visited[loc-1] = count+1
    if 0 <= loc+1 <= 100000 and visited[loc+1] == -1:
        q.append([loc+1, count+1])
        visited[loc+1] = count+1
    
    
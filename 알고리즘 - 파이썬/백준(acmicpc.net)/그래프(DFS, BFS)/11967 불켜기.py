import sys
from collections import deque
from collections import defaultdict
# input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().rstrip().split())
switch = defaultdict(list)
for _ in range(m):
    x, y, a, b = map(int, input().rstrip().split())
    switch[(x-1, y-1)].append((a-1, b-1))

bright = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]

bright[0][0] = 1
visited[0][0] = 1
result = 1

q = deque()
q.append([0, 0])

while q:
    x, y = q.popleft()
    
    for a, b in switch[(x, y)]:
        if not bright[a][b]:
            bright[a][b] = 1
            result += 1
            
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 1:
                    q.append([nx, ny])
                
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and bright[nx][ny] == 1:
            visited[nx][ny] = 1
            q.append([nx, ny])

print(result)
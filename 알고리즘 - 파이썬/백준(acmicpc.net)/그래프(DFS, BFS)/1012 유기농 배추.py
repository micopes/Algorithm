import sys
from collections import deque
# input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input().rstrip())
for t in range(T):
    
    m, n, k = map(int, input().rstrip().split())
    visited = [[0]*n for _ in range(m)]
    box = [[0]*n for _ in range(m)]
    q = deque()
    result = 0
    worm = []
    for i in range(k):
        x, y = map(int, input().rstrip().split())
        box[x][y] = 1
        worm.append([x, y])
    
    for i in range(len(worm)):
        x, y = worm[i][0], worm[i][1]
        if visited[x][y] == 0:
            q.append([x, y])
            visited[x][y] = 1
            result += 1
    
            while q:
                l = q.popleft()
                tempX = l[0]
                tempY = l[1]
                
                for j in range(4):
                    nx = tempX + dx[j]
                    ny = tempY + dy[j]
                    if 0 <= nx < m and 0 <= ny < n and \
                        visited[nx][ny] == 0 and box[nx][ny] == 1:
                            q.append([nx, ny])
                            visited[nx][ny] = 1
    print(result)

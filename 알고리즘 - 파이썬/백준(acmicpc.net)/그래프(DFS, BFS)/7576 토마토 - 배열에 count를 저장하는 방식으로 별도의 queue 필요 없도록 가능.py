from collections import deque
import sys
input = sys.stdin.readline

dqX = deque()
dqY = deque()
dqX2 = deque()
dqY2 = deque()

box = [[] for _ in range(1001)] # 1 ~ 1000

m, n = map(int, input().strip().split())

for i in range(n):
    data = list(map(int, input().strip().split()))
    for j in range(m):
        box[i].append(data[j])
        if box[i][j] == 1:
            dqX.append(i)
            dqY.append(j)
        
count = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
while len(dqX) > 0:
    while len(dqX) > 0:
        x = dqX.popleft()
        y = dqY.popleft()
        for i in range(4):
             kx = x + dx[i]
             ky = y + dy[i]
             if kx >= 0 and kx < n and ky >= 0 and ky < m and box[kx][ky] == 0:
                 box[kx][ky] = (box[x][y] + 1)
                 dqX.append(kx)
                 dqY.append(ky)
# 끝났는데 모든 토마토가 익지 않은 상태 -> -1 출력
result = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            result = -1
            break
        else:
            result = max(result, box[i][j])
    if result == -1:
        break

if result == -1:
    print(-1)
else:
    print(result-1)

        



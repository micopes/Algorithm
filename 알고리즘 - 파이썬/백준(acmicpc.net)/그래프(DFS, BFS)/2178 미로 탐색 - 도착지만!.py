import sys

from collections import deque
input = sys.stdin.readline

dqX = deque()
dqY = deque()

n, m = map(int, input().strip().split())

box = [[] for _ in range(100)]

for i in range(n):
    string = input().strip()
    for j in range(m):
        box[i].append(int(string[j]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dqX.append(0)
dqY.append(0)

while len(dqX) > 0:
    x = dqX.popleft()
    y = dqY.popleft()
    for i in range(4):
        kx = x + dx[i]
        ky = y + dy[i]
        if kx >= 0 and kx < n and \
            ky >= 0 and ky < m and box[kx][ky] == 1:
                box[kx][ky] = box[x][y] + 1
                dqX.append(kx)
                dqY.append(ky)

result = 1
print(box[n-1][m-1])
                
                    
                
        
        
        
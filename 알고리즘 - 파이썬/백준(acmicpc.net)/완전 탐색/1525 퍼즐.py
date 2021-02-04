from collections import deque
import sys
# input = sys.stdin.readline

def bfs():
    while q:
        d = q.popleft()
        if d == 123456789:
            print(dist[d])
            return
        s = str(d)
        index = s.index('9')
        x = index // 3
        y = index % 3
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue
            nk = nx*3 + ny
            temp = list(s)
            temp[nk], temp[index] = temp[index], temp[nk]
            temp = int(''.join(temp))
            if not dist.get(temp):
                dist[temp] = dist[d] + 1
                q.append(temp)
        
        
    print(-1)

tempList = []
for i in range(3):
    tempList.append(list(input().rstrip().split()))

box = ""
for i in range(3):
    for j in range(3):
        if tempList[i][j] == '0':
            box += '9'
        else:
            box += tempList[i][j]

box = int(box)
dist = dict()
dist[box] = 0
q = deque()
q.append(box)
bfs()
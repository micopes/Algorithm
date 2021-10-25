import sys
import copy
from collections import deque
from itertools import combinations
# input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(arr, selected, green):
    cnt = 0
    green_q = deque()
    red_q = deque()
    
    for r, c in selected:
        if [r, c] in green:
            green_q.append([r, c])
            arr[r][c] = 3
        else:
            red_q.append([r, c])
            arr[r][c] = 4

    # 한 색깔만 없어도 꽃이 안만들어지므로 종료되어도 된다.
    while green_q:
        green_temp = set()
        red_temp = set()
        while green_q:
            x, y = green_q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 1 or arr[nx][ny] == 2:
                        # set()은 tuple의 형식으로 넣어줘야 한다.
                        green_temp.add((nx, ny))
                        
        while red_q:
            x, y = red_q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 1 or arr[nx][ny] == 2:
                        # set()은 tuple의 형식으로 넣어줘야 한다.
                        red_temp.add((nx, ny))
                        
        inter = green_temp & red_temp
        green_temp = green_temp - inter
        red_temp = red_temp - inter
        
        for r, c in inter:
            arr[r][c] = 5
            cnt += 1
        for r, c in green_temp:
            arr[r][c] = 3
        for r, c in red_temp:
            arr[r][c] = 4
        
        green_q.extend(green_temp)
        red_q.extend(red_temp)
    
    return cnt
        
            

n, m, g, r = map(int, input().rstrip().split())

# 0 : 호수, 1 : 배양액 뿌릴 수 없는 땅, 2 : 배양액 뿌릴 수 있는 땅, 3 : green, 4 : red, 5 : flower
graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))

yellow = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            yellow.append([i, j])
            
ans = 0
for selected in combinations(yellow, (g+r)):
    for green in combinations(selected, g):
        arr = copy.deepcopy(graph)
        ans = max(ans, bfs(arr, selected, green))

print(ans)
            



# (0, 0) ~> (r-1, c-1)로 도달하는 것으로 idx 지정

# 1. 그람한테 가고, (r-1, c-1)과 (x, y)(그람의 위치)를 뺀 절댓값을 더한 거리
# 2. 바로 (r-1, c-1)까지 벽을 지나지 않고 이동하는 거리

# 1, 2 중 더 짧은 시간이 걸리는 것과 t를 비교하면 답을 구할 수 있다.

import sys
from collections import deque
# input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find1():
    visited = [[0]*c for _ in range(r)]

    q = deque()
    visited[0][0] = 1
    q.append([0, 0])
    
    while q:
        k = q.popleft()
        if k[0] == r-1 and k[1] == c-1:
            break
        for i in range(4):
            nr = k[0] + dr[i]
            nc = k[1] + dc[i]
            if 0 <= nr < r and 0 <= nc < c and visited[nr][nc] == 0 and (graph[nr][nc] == 0 or graph[nr][nc] == 2):
                visited[nr][nc] = visited[k[0]][k[1]] + 1
                q.append([nr, nc])
                
    if visited[r-1][c-1] != 0:
        return visited[r-1][c-1] - 1
    else:
        return -1

def find2():
    visited = [[0]*c for _ in range(r)]
    
    q = deque()
    visited[0][0] = 1
    q.append([0, 0])
    
    while q:
        k = q.popleft()
        if k[0] == gram_x and k[1] == gram_y:
            break
        for i in range(4):
            nr = k[0] + dr[i]
            nc = k[1] + dc[i]
            if 0 <= nr < r and 0 <= nc < c and visited[nr][nc] == 0 and (graph[nr][nc] == 0 or graph[nr][nc] == 2):
                visited[nr][nc] = visited[k[0]][k[1]] + 1
                q.append([nr, nc])
                
    if visited[gram_x][gram_y] != 0:
        return visited[gram_x][gram_y] + (r-1-gram_x) + (c-1-gram_y) - 1

    else:
        return -1
    

r, c, t = map(int, input().rstrip().split())

graph = []
for i in range(r):
    graph.append(list(map(int, input().rstrip().split())))

ans1 = find1()

gram_x, gram_y = 0, 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 2:
            gram_x, gram_y = i, j
            break
    if gram_x and gram_y:
        break

ans2 = find2()

# 도착을 못하는 경우도 생각을 해야 한다. -> 0이 뜬금없이 답이 될 수도 있으니.
# 0) 둘다 도달하지 못한 경우
if ans1 == -1 and ans2 == -1:
    print("Fail")
# 1) ans1이 도달하지 못한 경우 -> ans2가 시간 내에 도달한 것인지 확인하고 맞다면 최단시간 출력, 시간 내가 아니라면 fail
elif ans1 == -1:
    if ans2 <= t:
        print(ans2)
    else:
        print("Fail")
# 2) 1의 반대
elif ans2 == -1:
    if ans1 <= t:
        print(ans1)
    else:
        print("Fail")
# 3) 둘다 도달하는 경우 최소 시간과 비교하고, 시간 내에 도달 가능하다면 최소 시간을 출력
else:
    temp = min(ans1, ans2)
    if temp <= t:
        print(temp)
    else:
        print("Fail")
            
import sys
from collections import deque
# input = sys.stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(tx, ty):
    q = deque()
    q.append([tx, ty])
    visited = [ [0 for _ in range(col)] for __ in range(row)]
    visited[tx][ty] = 1
    count = 1
    
    while q:
        k = q.popleft()
        x = k[0]
        y = k[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < row and 0 <= ny < col and visited[nx][ny] == 0 and graph[x][y] == graph[nx][ny]:
                count += 1
                visited[nx][ny] = 1
                q.append([nx, ny])
    
    if count >= 4:
        for i in range(row):
            for j in range(col):
                if visited[i][j] == 1:
                    graph[i][j] = '.'
        return 1
    else:
        return 0
    
# 터진후 떨어뜨리는 함수                
def down():
    for j in range(col):
        q = deque()
        for i in range(row-1, -1, -1):
            if graph[i][j] != '.':
                q.append(graph[i][j])
        
        for i in range(row-1, -1, -1):
            if q:
                x = q.popleft()
                graph[i][j] = x
            else:
                graph[i][j] = '.'
                

# 입력
graph = []

for i in range(12):
    graph.append(list(input()))
    
row = 12
col = 6

# 풀이

answer = 0

while True:
    # flag 1번이라도 터지는 경우 1이상이 된다.
    flag = 0
    for i in range(12):
        for j in range(6):
            # 떨어진 경우 True로 만든다
            if graph[i][j] != '.':
                flag += bfs(i, j)
    
    # 모든 연쇄 가능한 것 터진 후에 떨어뜨린다.(여러 연쇄가 일어나도 떨어지기 전에는 하나로 본다.)
    down()
    if flag >= 1:
        answer += 1
    else:
        break

print(answer)
            
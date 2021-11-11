import sys
from collections import deque
# input = sys.stdin.readline

T = int(input().rstrip())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
key = []

for _ in range(T):
    h, w = map(int, input().rstrip().split())
    
    graph = []
    visited = [[0]*w for _ in range(h)]
    # 그래프
    for i in range(h):
        string = input().rstrip()
        graph.append(list(string))
    
    # 열쇠
    string = input().rstrip()
    key = list(string)
    
    # key를 KEY로 바꾸기
    for i in range(len(key)):
        key[i] = chr(ord(key[i]) - ord('a') + ord('A'))
    
    q = deque()
    ans = 0
# 테두리
    for i in range(h):
        if graph[i][0] == '.' or graph[i][0] in key or graph[i][0] == '$' or 'a' <= graph[i][0] <= 'z':
            q.append([i, 0])
            visited[i][0] = 1
            if graph[i][0] == '$':
                ans += 1
                graph[i][0] = '.'
            elif 'a' <= graph[i][0] <= 'z':
                key.append(chr(ord(graph[i][0]) - ord('a') + ord('A')))
                graph[i][0] = '.'
        elif 'A' <= graph[i][0] <= 'Z':
            visited[i][0] = 1

        if graph[i][w-1] == '.' or graph[i][w-1] in key or graph[i][w-1] == '$' or 'a' <=  graph[i][w-1] <= 'z':
            q.append([i, w-1])
            visited[i][w-1] = 1
            if graph[i][w-1] == '$':
                ans += 1
                graph[i][w-1] = '.'
            elif 'a' <= graph[i][w-1] <= 'z':
                key.append(chr(ord(graph[i][w-1]) - ord('a') + ord('A')))
                graph[i][w-1] = '.'
        elif 'A' <= graph[i][w-1] <= 'Z':
            visited[i][w-1] = 1
        
    for i in range(w):
        if graph[0][i] == '.' or graph[0][i] in key or graph[0][i] == '$' or 'a' <= graph[0][i] <= 'z':
            q.append([0, i])
            visited[0][i] = 1
            if graph[0][i] == '$':
                ans += 1
                graph[0][i] = '.'
            elif 'a' <= graph[0][i] <= 'z':
                key.append(chr(ord(graph[0][i]) - ord('a') + ord('A')))
                graph[0][i] = '.'
        elif 'A' <= graph[0][i] <= 'Z':
            visited[0][i] = 1
            
        if graph[h-1][i] == '.' or graph[h-1][i] in key or graph[h-1][i] == '$' or 'a' <= graph[h-1][i] <= 'z':
            q.append([h-1, i])
            visited[h-1][i] = 1
            if graph[h-1][i] == '$':
                ans += 1
                graph[h-1][i] = '.'
            elif 'a' <= graph[h-1][i] <= 'z':
                key.append(chr(ord(graph[h-1][i]) - ord('a') + ord('A')))
                graph[h-1][i] = '.'
        elif 'A' <= graph[h-1][i] <= 'Z':
            visited[h-1][i] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                # '.'으로 방문할 수 있는 경우 
                if visited[nx][ny] == 0 and graph[nx][ny] == '.':
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                # 대문자, key에 있고 방문 안한 경우
                elif visited[nx][ny] == 0 and graph[nx][ny] in key:
                    visited[nx][ny] = 1
                    graph[nx][ny] = '.'
                    q.append([nx, ny])
                # 대문자, key에 없고 방문 안한 경우
                elif visited[nx][ny] == 0 and graph[nx][ny] not in key and 'A' <= graph[nx][ny] <= 'Z':
                    visited[nx][ny] = 1
                # 소문자인 경우
                elif visited[nx][ny] == 0 and 'a' <= graph[nx][ny] <= 'z':
                    visited[nx][ny] = 1
                    tmp = chr(ord(graph[nx][ny]) - ord('a') + ord('A'))
                    graph[nx][ny] = '.'
                    key.append(tmp)
                    q.append([nx, ny])
                    # 대문자이고 방문했는데 key에 없었던 경우 -> key 새로 찾고 다시 방문
                    for a in range(h):
                        for b in range(w):
                            if graph[a][b] == tmp and visited[a][b] == 1:
                                q.append([a, b])
                                
                # 목표물
                elif visited[nx][ny] == 0 and graph[nx][ny] == '$':
                    visited[nx][ny] = 1
                    graph[nx][ny] = '.'
                    ans += 1
                    q.append([nx, ny])

    print(ans)
                    
                    
                
            
    
            
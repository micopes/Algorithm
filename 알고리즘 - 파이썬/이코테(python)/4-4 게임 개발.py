import sys
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) # n : 세로, m : 가로

X, Y, direct = map(int, input().rstrip().split())

# 0, 1, 2, 3 순으로
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

graph = []
visited = [[0]*m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))

visited[X][Y] = 1
while True:
    flag = False
    for _ in range(4):
        nx = X + dx[direct]
        ny = Y + dy[direct]
        if visited[nx][ny] == 0 and graph[nx][ny] == 0:
            visited[nx][ny] = 1
            X = nx
            Y = ny
            direct += 1
            direct %= 4
            flag = True
        else:
            direct += 1
            direct %= 4
    
    if flag == False:
        nx = X - dx[direct]
        ny = Y - dy[direct]
        if graph[nx][ny] == 1:
            break
        else:
            X = nx
            Y = ny

ans = 0
for i in range(len(visited)):
    ans += sum(visited[i])
    
print(ans)

    
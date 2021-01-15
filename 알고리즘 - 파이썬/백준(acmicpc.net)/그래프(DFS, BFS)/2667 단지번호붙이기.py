import sys
sys.setrecursionlimit(111111)

n = int(input())
number = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*n for _ in range(n)]
data = [[] for _ in range(n)] # 0 ~ n-1

def dfs(data, visited, x, y, val):
    global number
    visited[x][y] = number
    
    for i in range(4):
        kx = x + dx[i]
        ky = y + dy[i]
        if kx >= 0 and kx < n and ky >= 0 and ky < n:
            if visited[kx][ky] == 0 and data[kx][ky] == 1:
                dfs(data, visited, kx, ky, data[kx][ky])

for i in range(n):
    string = input()
    for j in range(n):
        data[i].append(int(string[j]))

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and data[i][j] == 1:
            dfs(data, visited, i, j, data[i][j])
            number += 1

result = [0 for _ in range(n*n+1)]
for i in range(n):
    for j in range(n):
        result[visited[i][j]] += 1
        
res = []
for i in range(1, len(result)):
    if result[i] == 0:
        break
    else:
        res.append(result[i])
        
print(len(res))
res.sort()
for i in range(len(res)):
    print(res[i])        
        
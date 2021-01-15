import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def dfs(data, visited, x, y):
    global n, m # [m][n]
    visited[x][y] = number
    
    for i in range(8):
        kx = x + dx[i]
        ky = y + dy[i]
        if kx >= 0 and kx < m and ky >= 0 and ky < n:
            if visited[kx][ky] == 0 and data[kx][ky] == 1:
                dfs(data, visited, kx, ky)
    return

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    visited = [[0]*n for _ in range(m)]
    data = [[] for _ in range(m)]
    number = 1 # 섬의 개수
    for i in range(m):
        list_ = list(map(int, input().split()))
        for j in range(len(list_)):
            data[i].append(list_[j])
    
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0 and data[i][j] == 1:
                dfs(data, visited, i, j)
                number += 1
                
    maxVal = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j] > maxVal:
                maxVal = visited[i][j]
    print(maxVal)
        
            
            
    
    

    
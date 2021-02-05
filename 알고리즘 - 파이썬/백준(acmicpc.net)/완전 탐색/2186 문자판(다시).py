import sys
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, idx):
    if idx == len(target):
        return 1
    if c[x][y][idx] != -1:
        return c[x][y][idx]
    
    c[x][y][idx] = 0
    for i in range(4):
        tempX, tempY = x, y
        for _ in range(k):
            nx = tempX + dx[i]
            ny = tempY + dy[i]  
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == target[idx]:
                    c[x][y][idx] += dfs(nx, ny, idx+1)
            tempX, tempY = nx, ny
    return c[x][y][idx]
        
        
    
n, m, k = map(int, input().rstrip().split())

a = []
for i in range(n):
    a.append(list(input().rstrip()))
    
target = list(input().rstrip())

result = 0
c = [[[-1]*len(target) for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == target[0]:
            result += dfs(i, j, 1)

print(result)

    
# BFS
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        def bfs(x, y):
            visited[x][y] = cnt
            
            q = deque()
            q.append((x, y))
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and grid[nx][ny] == '1':
                        visited[nx][ny] = cnt
                        q.append((nx, ny))
                    


        n = len(grid) # 행
        m = len(grid[0]) # 열
        visited = [[0]*m for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    cnt += 1
                    bfs(i, j)
        
        return cnt




        
        

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j, val):
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and grid[nx][ny] == '1':
                        q.append((nx, ny))
                        visited[nx][ny] = val
            return
        
        m = len(grid)
        n = len(grid[0])
        
        visited = [[0]*n for _ in range(m)]
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        val = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    bfs(i, j, val)
                    val += 1
                    
                    
        return val - 1
        
                    
                    
                    

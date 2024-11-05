from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        def bfs(x, y):
            visited[x][y] = 1
            cnt = 1 # 영역 크기

            q = deque()
            q.append((x, y))
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and grid[nx][ny] == 1:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                        cnt += 1

            return cnt
            
        n = len(grid)
        m = len(grid[0])

        visited = [[0]*m for _ in range(n)]

        max_cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    max_cnt = max(max_cnt, bfs(i, j))

        return max_cnt

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid[0])
        m = len(grid)


        visited = [[0]*n for _ in range(m)]
        cnt = 1
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    q = deque()
                    q.append([i, j])
                    visited[i][j] = cnt
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1' and visited[nx][ny] == 0:
                                q.append([nx, ny])
                                visited[nx][ny] = cnt
                    cnt += 1
        return cnt-1

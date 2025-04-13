class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        result = False

        def backtrack(x, y, substr):
            nonlocal result
            if substr != word[:len(substr)]:
                return
            
            if substr == word:
                result = True
                return
            
            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    backtrack(nx, ny, substr + board[nx][ny])
                    visited[nx][ny] = False

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    backtrack(i, j, board[i][j])
                    visited[i][j] = False

        return result

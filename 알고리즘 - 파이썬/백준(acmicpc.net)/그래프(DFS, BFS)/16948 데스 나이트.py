from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
n = int(input().rstrip())
r1, c1, r2, c2 = map(int, input().rstrip().split())
visited = [[0]*n for _ in range(n)] # 0 ~ n-1까지.

q = deque()
q.append([r1, c1])
visited[r1][c1] = 1

while q:
    x, y = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            q.append([nx, ny])
            visited[nx][ny] = visited[x][y] + 1

print(visited[r2][c2]-1) # 맨 처음 1로 시작했으므로 -1 필요 and 도착하지 못해서 0인 경우도 -1을 출력해줌.
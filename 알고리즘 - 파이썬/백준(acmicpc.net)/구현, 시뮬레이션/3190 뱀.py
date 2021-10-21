import sys
from collections import deque
# input = sys.stdin.readline

# [0, 1, 2, 3] : [오, 아래, 왼, 위]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0

snake = deque()
snake.append([1, 1]) # snake[0][0]이 snake_x, snake[0][1]이 snake_y
# snake_x, snake_y = 1, 1 # 뱀의 현재 위치

n = int(input().rstrip())
board = [[0]*(n+1) for _ in range(n+1)]

k = int(input().rstrip())
for i in range(k):
    x, y = map(int, input().rstrip().split())
    board[x][y] = 1

rotate = []
l = int(input().rstrip())
for i in range(l):
    x, c = input().rstrip().split()
    x = int(x)
    rotate.append([x, c])

second = 0
idx = 0
while True:
    # 이동할 곳
    nx = snake[0][0] + dx[d]
    ny = snake[0][1] + dy[d]
    
    # 벽이 아니고, 뱀의 일부도 아닌 경우 -> 이동 가능
    if 1 <= nx <= n and 1 <= ny <= n and [nx, ny] not in snake:
        # 사과인 경우 - 추가만 한다
        if board[nx][ny] == 1:
            snake.appendleft([nx, ny])
            board[nx][ny] = 0 # 사과를 없애야 한다.
        # 사과가 아닌 경우 - 머리 추가하고 꼬리 제거
        elif board[nx][ny] == 0:
            snake.appendleft([nx, ny])
            snake.pop()
    else:
        break
            
        
    # 이동 완료한 경우
    second += 1
    
    # 방향 전환 이후 것이 있을 때. 아니면 indexError 나올 수 있다
    if idx < len(rotate):
        # 방향 전환할 때가 된 경우
        if rotate[idx][0] == second:
            # 반시계방향 회전
            if rotate[idx][1] == 'L':
                d = (d-1) % 4
            # 시계방향 회전
            else:
                d = (d+1) % 4
            idx += 1

print(second+1)


    



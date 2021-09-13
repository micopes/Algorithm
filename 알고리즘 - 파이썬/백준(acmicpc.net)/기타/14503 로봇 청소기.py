import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

r, c, d = map(int, input().rstrip().split())

board = []

for i in range(n):
    board.append(list(map(int, input().rstrip().split())))

q = deque()
q.append([r, c, d])
    
# 북, 서, 남, 동 - 정해져있는거라서. 처음에 입력받을때도 방향이 정해져있다 임의로 조정 불가.
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0

# 0 : 청소 x, 1 : 벽, 2 : 청소 완료
while q:
    temp = q.popleft()
    r = temp[0]
    c = temp[1]
    d = temp[2]
    
    # 현재 위치 채우기
    if board[r][c] == 0:
        cnt += 1
        board[r][c] = 2
    
    flag = False # 4 방향 중 하나에 갈 수 있는 곳 있는 경우
    for _ in range(4):
        d = (d-1) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        if board[nr][nc] == 0:
            q.append([nr, nc, d])
            flag = True
            break

    # 네 방향 모두 청소가 되어있거나 벽인 경우
    if flag == False:
        # 후진 가능 경우
        if board[r-dr[d]][c-dc[d]] != 1:
            q.append([r-dr[d], c-dc[d], d])
    
        
print(cnt)
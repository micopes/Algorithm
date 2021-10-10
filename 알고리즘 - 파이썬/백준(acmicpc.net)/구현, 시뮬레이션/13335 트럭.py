import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().rstrip().split())
trucks = list(map(int, input().rstrip().split()))

time = 0
board_trucks = deque()
board_times = deque()
idx = 0

# 남은 트럭이 있는 동안에는 계속 진행
while idx < n:
    
    # 1. 시간 증가
    time += 1
    
    # 2. 건넌 것 없애기
    for i in range(len(board_times)):
        # 시간
        x = board_times.popleft()
        # 무게
        y = board_trucks.popleft()
        x -= 1
        # 건너지 못한 경우 넣고, 아니면 넣지 않는다.
        if x != 0:
            board_times.append(x)
            board_trucks.append(y)
            
            
    # 3. 탈 수 있다면 맨 뒤에 추가.
    # [무게, 건넌 시간(0되면 종료)]
    if sum(board_trucks) + trucks[idx] <= L:
        board_times.append(w)
        board_trucks.append(trucks[idx])
        idx += 1

print(time + max(board_times))
    
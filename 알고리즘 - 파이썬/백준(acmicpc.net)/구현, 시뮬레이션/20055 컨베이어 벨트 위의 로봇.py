import sys
from collections import deque
# input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

A = deque(list(map(int, input().rstrip().split())))

dq = deque()

for i in range(n):
    dq.append(0)

stage = 0
while True:
    stage += 1
    
    # 1. 1) 컨베이어 벨트 회전, 2)로봇 회전
    A.rotate(1)
    dq.rotate(1)
    dq[-1] = 0
    
    # 2. 먼저 들어온 것부터. 로봇을 회전, 이동할 수 없다면 가만히
    # 0 ~ N-1
    for i in range(n-2, -1, -1):
        if dq[i] == 1 and dq[i+1] == 0 and A[i+1] >= 1:
            dq[i] = 0
            dq[i+1] = 1
            A[i+1] -= 1
    
    # 내리는 위치 제거
    dq[-1] = 0
    
    # 3. 올리는 위치의 칸이 0이 아니면 올리는 위치에 로봇을 올린다
    if dq[0] == 0 and A[0] >= 1:
        dq[0] = 1
        A[0] -= 1
    
    cnt = 0
    for x in A:
        if x == 0:
            cnt += 1
    
    if cnt >= k:
        break
    
print(stage)
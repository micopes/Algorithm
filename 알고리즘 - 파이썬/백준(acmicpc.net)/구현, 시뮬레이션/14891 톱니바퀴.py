from collections import deque
import sys
input = sys.stdin.readline

def check_left(num, d):
    if num >= 0 and q[num][2] != q[num+1][6]:
        check_left(num-1, -d)
        q[num].rotate(d)

def check_right(num, d):
    if num <= 3 and q[num-1][2] != q[num][6]:
        check_right(num+1, -d)
        q[num].rotate(d)
    

q1 = deque(list(input().rstrip()))
q2 = deque(list(input().rstrip()))
q3 = deque(list(input().rstrip()))
q4 = deque(list(input().rstrip()))

q = []
q.append(q1)
q.append(q2)
q.append(q3)
q.append(q4)

k = int(input().rstrip())
for i in range(k):
    num, d = map(int, input().rstrip().split())
    # 1 ~ 4를 0 ~ 3으로 변경
    num -= 1
    
    # 해당 방향의 톱니바퀴가 움직여야 하는지 점검
    check_left(num-1, -d)
    check_right(num+1, -d)
    
    # 점검 끝났으므로 현재 톱니바퀴 변경
    q[num].rotate(d)

score = 0
for i in range(4):
    if q[i][0] == '1':
        score += 2**i

print(score)

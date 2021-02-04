from collections import deque
import sys
# input = sys.stdin.readline

n = int(input().rstrip())
dq = deque()
for i in range(1, n+1):
    dq.append(i)

result = -1
while dq:
    if len(dq) == 1:
        result = dq.popleft()
        break
    dq.popleft()
    dq.append(dq.popleft())
    
    
print(result) # 제일 마지막에 나온 것. IndexError만 아니라면 괜찮다.
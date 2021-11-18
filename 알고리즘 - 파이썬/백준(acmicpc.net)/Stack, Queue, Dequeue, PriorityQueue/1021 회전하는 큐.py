from collections import deque
import sys
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
val_list = list(map(int, input().rstrip().split()))

q = deque()
for i in range(1, n+1):
    q.append(i)

cnt = 0
for x in val_list:
    while True:
        if q.index(x) == 0:
            q.popleft()
            break
        
        if q.index(x) < len(q) - q.index(x):
            q.rotate(-1) # q.append(q.popleft())
            cnt += 1
        else:
            q.rotate(1) # q.appendleft(q.pop())
            cnt += 1
    
print(cnt)
            


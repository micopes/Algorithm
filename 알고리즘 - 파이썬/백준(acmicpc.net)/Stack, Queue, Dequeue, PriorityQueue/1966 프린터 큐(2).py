import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n, m = map(int, input().rstrip().split()) # 문서의 개수 n, 궁금한 것이 m번째 놓인 것 표시(0 ~ n-1)
    data = list(map(int, input().rstrip().split()))
    q = deque()
    for i in range(len(data)):
        q.append([data[i], i])
    
    cnt = 1
    while q:
        x = q.popleft()
        if len(q) == 0:
            print(cnt)
        elif max(q)[0] <= x[0]:
            if x[1] == m:
                print(cnt)
                break
            cnt += 1
        else:
            q.append(x)
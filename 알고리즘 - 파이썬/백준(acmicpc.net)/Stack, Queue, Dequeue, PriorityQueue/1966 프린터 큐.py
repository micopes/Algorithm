from collections import deque
import sys
# input = sys.stdin.readline

T = int(input().rstrip())

for t in range(T):
    n, m = map(int, input().rstrip().split())
    list_ = list(map(int, input().rstrip().split()))
    dq = deque()
    for i in range(len(list_)):
        dq.append([i, list_[i]]) # i번째 놈
        
    count = 0
    while dq:
        x = dq[0]
        if max(dq, key = lambda x : x[1])[1] == x[1]:
            count += 1
            dq.popleft()
            if x[0] == m:
                print(count)
                break
        else:
            dq.popleft()
            dq.append(x)
        
            
            
    
    
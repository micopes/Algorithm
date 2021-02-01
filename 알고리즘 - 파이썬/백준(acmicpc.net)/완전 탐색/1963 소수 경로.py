import sys
import math
from collections import deque
input = sys.stdin.readline

sosu = [1 for _ in range(10000)] # 1000 ~ 9999
sosu[1] = 0
sosu[2] = 1
sosu[3] = 1
for i in range(4, 10000):
    end = int(math.sqrt(i))
    for j in range(2, end+1):
        if i % j == 0:
            sosu[i] = 0
            break


T = int(input().strip())

for t in range(T):
    visited = [0 for _ in range(10000)]
    dist = [0 for _ in range(10000)]
    x, y = input().strip().split()
    dist[int(x)] = 1
    dq = deque()
    dq.append(x)
    while dq:
        temp = dq.popleft() # string
        if temp == y:
            break
        # 천의 자리
        for i in range(1, 10): # 1 ~ 9
            if temp[0] == i:
                continue
            k = ""
            k += str(i) # 0
            k += temp[1::] # 1 2 3
            k = int(k)
            if sosu[k] == 1 and dist[k] == 0:
                dist[k]= dist[int(temp)] + 1
                dq.append(str(k))
        # 백의 자리
        for i in range(0, 10): # 0 ~ 9
            if temp[1] == i:
                continue
            k = ""
            k += temp[0] # 0
            k += str(i) # 1
            k += temp[2::] # 2 3
            k = int(k)
            if sosu[k] == 1 and dist[k] == 0:
                dist[k] = dist[int(temp)] + 1
                dq.append(str(k))
        # 십의 자리
        for i in range(0, 10): # 0 ~ 9
            if temp[2] == i:
                continue
            k = ""
            k += temp[0:2] # 0 1
            k += str(i) # 2 
            k += temp[3] # 3
            k = int(k)
            if sosu[k] == 1 and dist[k] == 0:
                dist[k] = dist[int(temp)] + 1
                dq.append(str(k))
        # 일의 자리
        for i in [1, 3, 5, 7, 9]:
            if temp[3] == i:
                continue
            k = ""
            k += temp[0:3] # 0 1 2
            k += str(i) # 3
            k = int(k)
            if sosu[k] == 1 and dist[k] == 0:
                dist[k] = dist[int(temp)] + 1
                dq.append(str(k))
        
        
    print(dist[int(y)]-1)
    
import sys
from collections import deque
# input = sys.stdin.readline

T = int(input().rstrip())
for t in range(T):
    dist = ["" for _ in range(10000)]
    visited = [0 for _ in range(10000)]
    x, target = map(int, input().rstrip().split())
    
    dq = deque()
    dq.append(x)
    while True:
        n = dq.popleft()
        # D
        if n == 0: # 반례 0 1000 -> 0 * 0 = 0을 방문처리해 D가 앞에 붙게된다.
            pass
        else:
            temp = n*2 
            if temp > 9999:
                temp %= 10000
            if visited[temp] == 0: 
                dist[temp] += (dist[n] + 'D')
                visited[temp] = 1
                dq.append(temp)
                if temp == target:
                    print(dist[temp])
                    break
        # S
        if n == 0:
            temp = 9999
        else:
            temp = n-1
        if visited[temp] == 0: 
            dist[temp] += (dist[n] + 'S')
            visited[temp] = 1
            dq.append(temp)
            if temp == target:
                print(dist[temp])
                break
        # L
        k = str(n)
        if len(k) == 1:
            k = k[0] + '0'
        elif 2 <= len(k) <= 3:
            k = k[0::] + '0'
        elif len(k) == 4:
            k = k[1::] + k[0]
        temp = int(k)
        if visited[temp] == 0: 
            dist[temp] += (dist[n] + 'L')
            visited[temp] = 1
            dq.append(temp)
            if temp == target:
                print(dist[temp])
                break
        # R
        k = str(n)
        if len(k) == 1:
            k = k[0] + '000'
        elif len(k) == 2:
            k = k[-1] + '00' + k[0]
        elif len(k) == 3:
            k = k[-1] + '0' + k[0:-1]
        elif len(k) == 4:
            k = k[-1] + k[0:-1]
        temp = int(k)
        if visited[temp] == 0: 
            dist[temp] += (dist[n] + 'R')
            visited[temp] = 1
            dq.append(temp)
            if temp == target:
                print(dist[temp])
                break
        
    
    
    
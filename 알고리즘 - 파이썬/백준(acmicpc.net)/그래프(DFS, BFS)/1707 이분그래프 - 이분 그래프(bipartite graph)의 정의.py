import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

for k in range(K):
    visited = [0 for _ in range(20001)]
    graph = [[] for _ in range(20001)]
    
    v, e = map(int, input().split())
    
    for i in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    result = 1
    for l in range(1, v+1):
        if visited[l] != 0:
            continue
        
        dq = deque([l])
        visited[l] = 1
        
        while len(dq) != 0:
            x = dq.popleft()
            for i in graph[x]:
                if visited[x] == 1:
                    if visited[i] == 1:
                        result = 0
                        break
                    elif visited[i] == 0:
                        visited[i] = 2
                        dq.append(i)
                else:
                    if visited[i] == 2:
                        result = 0
                        break
                    elif visited[i] == 0:
                        visited[i] = 1
                        dq.append(i)
            if result == 0:
                break
        
    if result == 0:
        print("NO")
    else:
        print("YES")
    
    
        
            
            
        
        
    
    
    
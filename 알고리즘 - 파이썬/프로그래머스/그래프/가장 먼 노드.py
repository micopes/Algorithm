from collections import deque

def solution(n, vertex):
    answer = 0
    visited = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)] # 1 ~ n
    
    for k in vertex:
        x = k[0]
        y = k[1]
        graph[x].append(y)
        graph[y].append(x)
    
    q = deque()
    q.append(1)
    visited[1] = 1 # 1이 방문, 0이 미방문
    
    while q:
        k = q.popleft()
        for x in graph[k]:
            if visited[x] == 0:
                visited[x] = visited[k] + 1
                q.append(x)
            
        
    for i in range(1, n+1):
        if visited[i] == max(visited):
            answer += 1
    
    
    return answer
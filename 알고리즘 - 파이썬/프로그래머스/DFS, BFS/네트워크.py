from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [0]*n
    q = deque()
    
    for i in range(n):
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1
            answer += 1
            
            while q:
                x = q.popleft()
                for j in range(n):
                    if visited[j] == 0 and computers[x][j] == 1:
                        q.append(j)
                        visited[j] = 1
    
    return answer
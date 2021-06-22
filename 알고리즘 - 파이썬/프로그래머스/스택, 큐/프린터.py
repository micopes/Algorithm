from collections import deque

def solution(priorities, location):
    q = deque()
    
    for i in range(len(priorities)):
        q.append([i, priorities[i]])
        
    cnt = 0
    while q:
        x = q[0]
        if x[1] == max(q, key = lambda x : x[1])[1]:
            q.popleft()
            cnt += 1
            if location == x[0]:
                return cnt
        else:
            q.append(q.popleft())
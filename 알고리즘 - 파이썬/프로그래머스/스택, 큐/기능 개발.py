from collections import deque

def solution(progresses, speeds):
    answer = []
    
    q = deque()
    for i in range(len(progresses)):
        temp = (100-progresses[i]) // speeds[i]
        if (100-progresses[i]) % speeds[i] != 0:
            temp += 1
        q.append(temp)
    
    while q:
        num = 1 # 배포 개수
        x = q.popleft()
        
        while q and x >= q[0]:
            q.popleft()
            num += 1
        
        answer.append(num)    
            
    return answer
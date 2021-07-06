def solution(n, lost, reserve):
    answer = 0
    
    uniform = []
    for i in range(n): # 각자 1개씩
        uniform.append(1)
    
    for x in lost: # 도난
        uniform[x-1] -= 1
    
    for x in reserve: # 여분
        uniform[x-1] += 1
    
    # 앞에 먼저 채워주고 그다음 뒤를 채워준다.
    for i in range(1, n):
        if uniform[i] == 2 and uniform[i-1] == 0:
            uniform[i-1] = uniform[i] = 1
        
    for i in range(0, n-1):
        if uniform[i+1] == 0 and uniform[i] == 2:
            uniform[i+1] = uniform[i] = 1
    
    for i in range(n):
        if uniform[i] >= 1:
            answer += 1
        
    
    return answer
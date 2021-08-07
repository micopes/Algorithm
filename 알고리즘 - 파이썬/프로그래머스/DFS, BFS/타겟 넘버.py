# +, -를 적절하게 해서 타겟 넘버가 성립하는지를 계산하면 된다.

from collections import deque
    
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([0, 0]) # (target이 되는 수, len)
    
    while q:
        x = q.popleft()
        val = x[0]
        length = x[1]
        # x[0], x[1]
        if length < len(numbers):
            q.append([val + numbers[length], length+1])
            q.append([val - numbers[length], length+1])
            length += 1
        else: # 길이가 같을 때
            if val == target:
                answer += 1
    
    return answer
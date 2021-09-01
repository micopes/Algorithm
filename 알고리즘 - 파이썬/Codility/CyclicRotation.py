from collections import deque
def solution(A, K):
    # 빈 배열인 경우 확인 필요. 아래에서 % 0을 하면 runtime error 발생.
    if len(A) == 0:
        return []

    dq = deque()

    for x in A:
        dq.append(x)
    
    it = K % len(A)

    for i in range(it):
        temp = dq.pop()
        dq.appendleft(temp)
    
    ans = []
    while dq:
        x = dq.popleft()
        ans.append(x)
    
    return ans
def solution(brown, yellow):
    answer = []
    
    # M : 가로, N : 세로 (M >= N)
    MplusN = (brown + 4) // 2
    MmultiN = brown + yellow
    
    for i in range(1, MplusN+1): # N : 세로
        j = MplusN - i # M : 가로
        if i*j == MmultiN:
            answer.append(j)
            answer.append(i)
            break
    
    return answer
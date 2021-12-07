def solution(brown, red):
    answer = []
    
    flag = False
    for i in range(5001):
        for j in range(i+1):
            if i*j == brown+red and (i-2)*(j-2) == red:
                flag = True
                answer = [i, j]
                break
        if flag == True:
            break
    
    return answer
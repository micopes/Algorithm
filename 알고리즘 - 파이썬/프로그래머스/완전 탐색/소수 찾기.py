import math
from itertools import permutations

def solution(numbers):
    answer = 0
    
    ans_list = []
    
    for i in range(1, len(numbers)+1):
        permute = permutations(numbers, i) 
        li = list(permute)
        
        for j in range(len(li)):
            ans_list.append(int("".join(li[j])))
    
    ans_list = list(set(ans_list)) # 중복 제거
    
    for i in range(len(ans_list)):
        temp = ans_list[i]
        flag = 1 # 소수가 맞다.
        for j in range(2, int(math.sqrt(temp))+1):
            if temp % j == 0: # 나누어 떨어지는 수가 있으면
                flag = 0 # 소수가 아니다.
                break
                
        if temp == 1 or temp == 0:
            flag = 0
            
        if flag == 1:
            answer += 1
            print(temp)
        
    return answer

    


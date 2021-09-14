import sys
from collections import deque
# input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    command = input().rstrip()
    command_list = list(command)
    n = int(input())
    
    dq = deque()
    # 문자열 -> 리스트
    temp = input()
    temp = temp[1:-1].split(',')
    
    for i in range(n):
        dq.append(temp[i])
        
    di = 0 # 방향
    is_error = False
    for i in range(len(command_list)):
        if command_list[i] == 'D' and len(dq) == 0:
            is_error = True
            break
        elif command_list[i] == 'D' and di == 0:
            dq.popleft()
        elif command_list[i] == 'D' and di == 1:
            dq.pop()
        elif command_list[i] == 'R':
            if di == 0:
                di = 1
            else:
                di = 0
                
    ans_list = []
    if is_error == True:
        print("error")
    else:
        if di == 0:
            while dq:
                x = dq.popleft()
                ans_list.append(x)
        else:
            while dq:
                x = dq.pop()
                ans_list.append(x)
    
        # 출력
        print('[', end = "")
        for i in range(len(ans_list)):
            if i != len(ans_list)-1:
                print(ans_list[i], end = ",")
            else:
                print(ans_list[i], end = "")
        print(']')
            
            
        
            
        
    
    
    
    
        
    
    
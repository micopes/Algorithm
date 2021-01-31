import sys
input = sys.stdin.readline

n = int(input().strip())

plus = []
zero = False
minus = []
result = 0

for i in range(n):
    x = int(input().strip())
    if x > 0:
        plus.append(x)
    elif x < 0:
        minus.append(x)
    else:
        zero = True
        

plus.sort(reverse = True)
temp1 = 0
val = 1
num = 1
for i in range(len(plus)):
    if plus[i] == 1: # 1이면 그냥 더한다
        temp1 += 1
    else: # 그 외의 숫자라면 val에 저장
        if num == 1 and val == 1:
            val = plus[i]
            num = 2
        elif num == 2:
            val *= plus[i]
            temp1 += val
            val = 1
            num = 1
if num == 2: # 다 끝나고 1개 남은 경우
    temp1 += val
result += temp1
    
minus.sort() # -7, -6, -5 ...
temp2 = 0
val = 1
num = 1
if len(minus) == 0:
    pass
elif len(minus) % 2 == 0: # 짝수개.
    for i in range(len(minus)):
        if num == 1 and val == 1:
            val = minus[i]
            num = 2
        elif num == 2:
            val *= minus[i]
            temp2 += val
            val = 1
            num = 1
else: # 홀수개
    for i in range(len(minus)):
        if num == 1 and val == 1:
            val = minus[i]
            num = 2
        elif num == 2:
            val *= minus[i]
            temp2 += val
            val = 1
            num = 1
    if num == 2:
        if zero == True:
            pass # 아무것도 안더해도 됨
        else:
            result += val
result += temp2
        
print(result)

            
            
    
    
    
    
    
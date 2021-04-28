import sys
from collections import deque
# input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    string = input().rstrip()
    q = deque()
    for c in string:
        q.append(c)
    
    flag = True
    cnt = 0 # '('의 개수
    while len(q):
        x = q.popleft()
        
        if x == '(':
            cnt += 1
        elif x == ')':
            cnt -= 1
            if cnt < 0:
                flag = False
                break
    
    if cnt != 0:
        flag = False
        
    if flag == True:
        print("YES")
    else:
        print("NO")
        
        
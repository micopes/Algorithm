import sys
# input = sys.stdin.readline

n = int(input().rstrip())
top = list(map(int, input().rstrip().split()))
stack = [] # [idx, val]

for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            print(stack[-1][0] + 1, end = " ")
            break
        else:
            stack.pop()
    
    if len(stack) == 0:
        print(0, end = " ")
        
    stack.append([i, top[i]])
        
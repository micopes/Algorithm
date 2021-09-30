import sys
# input = sys.stdin.readline

while True:
    numbers = list(map(int, input().rstrip().split()))
    n = numbers.pop(0)
    
    if n == 0:
        break
    
    stack = []
    
    answer = 0
    for i in range(n):
        while stack and numbers[stack[-1]] > numbers[i]:
            idx = stack.pop()
            
            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            
            answer = max(answer, width * numbers[idx])
        
        stack.append(i)
    
    
    while stack:
        idx = stack.pop()
        
        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
            
        answer = max(answer, width * numbers[idx])
    
    print(answer)
        

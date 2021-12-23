import sys
# input = sys.stdin.readline

n = int(input().rstrip())

cnt = 0
for _ in range(n):
    string = input().rstrip()
    
    stack = []
    for ch in string:
        # 스택이 비어있다면 넣는다.
        if len(stack) == 0:
            stack.append(ch)
        # stack top과 ch가 다르면 stack에 넣는다.
        elif stack[-1] != ch:
            stack.append(ch)
        # stack top과 ch가 같으면 stack에서 뺀다.
        else:
            stack.pop()
        
    # 스택에 남아있는 것이 없으면 cnt추가
    if len(stack) == 0:
        cnt += 1

print(cnt)
            
            
    
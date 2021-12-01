import sys
# input = sys.stdin.readline

n = int(input().rstrip())
li = []

for _ in range(n):
    b = int(input().rstrip())
    li.append(b)
    
stack = []
ans = 0
for i in range(n):
    while stack and stack[-1] <= li[i]:
        stack.pop()
    stack.append(li[i])
    ans += len(stack)-1
print(ans)
    


            
    
    


    
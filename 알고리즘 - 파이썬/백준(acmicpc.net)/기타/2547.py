import sys
# input = sys.stdin.readline

T = int(input().strip())

for t in range(T):
    input()
    n = int(input().strip())
    candy = []
    for i in range(n):
        x = int(input().strip())
        candy.append(x)
        
    if sum(candy) % n == 0:
        print("YES")
    else:
        print("NO")
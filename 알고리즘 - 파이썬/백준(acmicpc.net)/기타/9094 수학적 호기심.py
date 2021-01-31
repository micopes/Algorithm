import sys
input = sys.stdin.readline

T = int(input().strip())

for k in range(T):
    num = 0 
    n, m = map(int, input().strip().split())
    for a in range(1, n):
        for b in range(a+1, n):
            if (a**2 + b**2 + m) // (a*b) == (a**2 + b**2 + m) / (a*b):
                num += 1
    print(num)
            
    
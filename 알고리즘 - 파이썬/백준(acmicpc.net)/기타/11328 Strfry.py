import sys
# input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n):
    a, b = input().rstrip().split()
    a = list(a)
    b = list(b)
    
    a.sort()
    b.sort()
    
    if a == b:
        print("Possible")
    else:
        print("Impossible")
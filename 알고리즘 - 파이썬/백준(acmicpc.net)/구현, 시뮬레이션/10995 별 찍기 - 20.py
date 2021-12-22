import sys
# input = sys.stdin.readline

n = int(input().rstrip())


for i in range(1, n+1):
    if i % 2 == 1:
        for j in range(n):
            print("* ", end = "")
        print()
    else:
        for j in range(n):
            print(" *", end = "")
        print()
        

import sys
# input = sys.stdin.readline

n = int(input().strip())

for k in range(n):
    a, b = map(int, input().strip().split())
    temp = a % 10
    for i in range(1, b):
        temp *= a
        temp %= 10
    if temp == 0:
        temp = 10
    print(temp)
    
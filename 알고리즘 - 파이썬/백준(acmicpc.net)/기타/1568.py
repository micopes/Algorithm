import sys
# input = sys.stdin.readline

n = int(input().strip())

second = 0
k = 1
while n > 0:
    if k > n:
        k = 1
    n -= k
    k += 1
    second += 1

print(second)
    
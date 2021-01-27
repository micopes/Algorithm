import sys
# input = sys.stdin.readline

n, m = map(int, input().strip().split())

result = 0
if n == 1:
    result = 1
elif n == 2:
    result = min((m + 1)//2, 4)
else:
    if m >= 7:
        result = m-2
    else:
        result = min(m, 4)

print(result)
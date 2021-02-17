import sys
input = sys.stdin.readline

n, s = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))

result = 100000 # 길이
start, end, total = 0, 0, 0

while True:
    if total >= s:
        total -= a[start]
        start += 1
    elif end == n:
        break
    else:
        total += a[end]
        end += 1
        
    length = end - start
    if length < result and total >= s:
        result = length

if result == 100000:
    print(0)
else:
    print(result)
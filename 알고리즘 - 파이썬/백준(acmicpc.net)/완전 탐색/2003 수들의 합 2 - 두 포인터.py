import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))

total, s, e, cnt = 0, 0, 0, 0
while True:
    if m <= total:
        total -= a[s]
        s += 1
    elif e == n: # index 초과.
        break
    else:
        total += a[e]
        e += 1
    
    if total == m:
        cnt += 1

print(cnt)
        
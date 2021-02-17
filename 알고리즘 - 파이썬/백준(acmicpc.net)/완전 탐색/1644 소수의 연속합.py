import sys
import math
input = sys.stdin.readline

n = int(input().rstrip())
sosu = [1 for _ in range(n+5)] # IndexError 방지

sosu[0] = 0
sosu[1] = 0
sosu[2] = 1
sosu[3] = 1

for i in range(4, n+1, 2):
    if i % 2 == 0:
       sosu[i] = 0
    
for i in range(5, n+1, 2):
    for j in range(3, int(math.sqrt(i))+1, 2):
        if i % j == 0:
            sosu[i] = 0
            break
a = []
for i in range(2, n+1):
    if sosu[i] == 1:
        a.append(i)

start, end, cnt, total = 0, 0, 0, 0
while True:
    if total >= n:
        total -= a[start]
        start += 1
    elif end == len(a):
        break
    else:
        total += a[end]
        end += 1
    
    if n == total:
        cnt += 1
    
print(cnt)
        
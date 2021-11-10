import sys
import math
input = sys.stdin.readline
n = 10000001
prime = [True]*(n)
prime[0] = False
prime[1] = False
prime[2] = True

for i in range(2, int(math.sqrt(n)+1)):
    # i가 소수가 아니라면 앞서서 이미 prime[j]는 제거되었을 것.
    if not prime[i]:
        continue
    for j in range(2*i, n, i):
        prime[j] = False

a, b = map(int, input().rstrip().split())
cnt = 0

for i in range(2, n):
    if not prime[i]:
        continue
    
    mul = i*i
    while mul <= b:
        if a <= mul:
            cnt += 1
        mul *= i

print(cnt)
        
            
import math
import sys
input = sys.stdin.readline

sosu = [1 for _ in range(1000001)]
sosu[1] = 0
sosu[2] = 1
sosu[3] = 1

for i in range(4, 1000001):
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            sosu[i] = 0
            break
# 홀수 소수기 때문에 나중에 2는 제외해줘야 한다.
sosu[2] = 0

n = True
while n != 0:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(3, int(n/2)+1, 2):
            if sosu[i] == 1 and sosu[n-i] == 1:
                print("%d = %d + %d" % (n, i, n-i))
                break
    


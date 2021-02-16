import sys
import math
input = sys.stdin.readline

sosu = [1 for _ in range(2000)]

sosu[1] = 1
sosu[2] = 1
sosu[3] = 1

for i in range(4, 2000):
    if i % 2 == 0:
        sosu[i] = 0
        continue
    for j in range(3, int(math.sqrt(i)), 2):
        if i % j == 0:
            sosu[i] = 0
            break

string = input().rstrip()
total = 0
for i in string:
    if 'a' <= i <= 'z':
        total += (ord(i) - ord('a') + 1)
    else:
        total += (ord(i) - ord('A') + 1)

if sosu[total] == 1:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
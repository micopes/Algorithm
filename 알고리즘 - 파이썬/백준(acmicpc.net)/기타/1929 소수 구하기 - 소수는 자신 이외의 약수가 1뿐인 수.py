import math

sosu = [1 for _ in range(1000001)]
sosu[1] = 0
sosu[2] = 1
sosu[3] = 1

M, N = map(int, input().split())

for i in range(4, N+1):
    end = int(math.sqrt(i))
    for j in range(2, end+1):
        if i % j == 0:
            sosu[i] = 0
            break
        
for i in range(M, N+1):
    if sosu[i] == 1 :
        print(i)

        
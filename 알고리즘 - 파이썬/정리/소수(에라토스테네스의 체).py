import math

n = int(input().rstrip())
prime = [True for _ in range(n+1)]

prime[0] = False
prime[1] = False
prime[2] = True

for i in range(2, int(math.sqrt(n))+1):
    # 이미 제거한 배수
    if prime[i] == False:
        continue
    for j in range(i*2, n+1, i):
        prime[i] = False
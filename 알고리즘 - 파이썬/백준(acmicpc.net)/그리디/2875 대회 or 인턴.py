import sys
input = sys.stdin.readline

n, m, k = map(int, input().strip().split())

guitar = 0
result = 0
while True:
    if n > m*2:
        n -= 1
        guitar += 1
    elif n == m*2:
        break
    else:
        m -= 1
        guitar += 1

result = m

while True:
    if guitar >= k:
        break
    else:
        guitar += 3
        result -= 1
        
if result < 0:
    print(0)
else:
    print(result)
    
    
    
        

        

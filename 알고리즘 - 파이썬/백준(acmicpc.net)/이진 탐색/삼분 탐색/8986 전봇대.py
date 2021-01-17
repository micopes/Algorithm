import sys
# input = sys.stdin.readline

def moveDist(x0):
    result = 0
    for i in range(1, n):
        result += abs(x0*i - x[i])
    return result

n = int(input().strip())
x = list(map(int, input().strip().split()))

start, end = 0, x[n-1]

while end - start >= 3:
    p = (start*2+end) // 3
    q = (start+end*2) // 3
    if moveDist(p) <= moveDist(q):
        end = q
    else:
        start = p

result = 10000000000000000000
for i in range(start, end+1):
    result = min(result, moveDist(i))
    
print(result)
    
    

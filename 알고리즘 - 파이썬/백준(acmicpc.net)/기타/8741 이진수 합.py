import sys
input = sys.stdin.readline

n = int(input().rstrip())

res = []
for i in range(n):
    res.append('1')
for i in range(n-1):
    res.append('0')

print(''.join(res))
    

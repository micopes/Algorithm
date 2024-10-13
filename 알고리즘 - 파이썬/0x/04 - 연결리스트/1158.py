import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

q = deque()

for i in range(1, n+1):
    q.append(i)

result = "<"

idx = 0
while q:
    x = q.popleft()
    idx = (idx + 1) % k

    if idx == 0:
        result = result + str(x) + ", "
    else:
        q.append(x)

result = result[:-2]
result += ">"

print(result)

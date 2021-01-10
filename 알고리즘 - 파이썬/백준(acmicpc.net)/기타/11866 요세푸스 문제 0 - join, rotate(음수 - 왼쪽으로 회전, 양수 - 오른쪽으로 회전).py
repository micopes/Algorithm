import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
d = deque([i for i in range(1, n+1)])
res = []

while d:
    d.rotate(-k+1) # 음수이면 왼쪽으로 회전, 양수이면 오른쪽으로 회전
    res.append(str(d.popleft()))
    
print("<" + ", ".join(res) + ">")

    
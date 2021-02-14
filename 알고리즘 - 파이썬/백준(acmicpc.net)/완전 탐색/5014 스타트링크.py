import sys
from collections import deque
input = sys.stdin.readline

def bfs(S):
    c[S] = 1
    q.append([S, 0]) # 현재 층 위치, 횟수
    while q:
        x, cnt = q.popleft()
        if x == G:
            return 
        toUp = x + U
        toDown = x - D
        if toUp <= F and c[toUp] == 0:
            q.append([toUp, cnt+1])
            c[toUp] = cnt + 1
        if toDown >= 1 and c[toDown] == 0: 
            q.append([toDown, cnt+1])
            c[toDown] = cnt + 1
    
F, S, G, U, D = map(int, input().rstrip().split())
q = deque()
c = [0 for _ in range(1000001)]
bfs(S)

if S == G:
    print(0)
elif c[G] != 0:
    print(c[G]) # 처음에 1로 시작했기 때문에
else:
    print("use the stairs")
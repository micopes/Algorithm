import sys
# input = sys.stdin.readline

def bfs(n, cnt):
    global ans
    temp1 = n*2
    temp2 = n*10 + 1
    if temp1 == B or temp2 == B:
        ans = cnt
        return
    else:
        if temp1 < B:
            bfs(temp1, cnt+1)
        if temp2 < B:
            bfs(temp2, cnt+1)
    
A, B = map(int, input().rstrip().split())
ans = 0
bfs(A, 2)
if ans == 0:
    print(-1)
else:
    print(ans)
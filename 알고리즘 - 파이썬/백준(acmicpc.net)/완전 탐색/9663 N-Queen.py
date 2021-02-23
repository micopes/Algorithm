import sys
# input = sys.stdin.readline

n = int(input().rstrip())
ans = 0

a, b, c = [0]*n, [0]*(2*n), [0]*(2*n)

def backtrack(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not (a[j] == 1 or b[i+j] == 1 or c[n-j+i] == 1):
            a[j], b[i+j], c[n-j+i] = 1, 1, 1
            backtrack(i+1)
            a[j], b[i+j], c[n-j+i] = 0, 0, 0

backtrack(0)
print(ans)
        
import sys
# input = sys.stdin.readline

n = int(input().rstrip())
ans = 0
for i in range(1, n+1):
    if i**2 <= n:
        ans += 1

print(ans)
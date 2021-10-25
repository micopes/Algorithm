import sys
# input = sys.stdin.readline

n = int(input().rstrip())

level = []
for i in range(n):
    x = int(input().rstrip())
    level.append(x)

ans = 0
for i in range(n-2, -1, -1):
    if level[i+1] <= level[i]:
        ans += (level[i] - level[i+1] + 1)
        level[i] = level[i+1] - 1

print(ans)

        


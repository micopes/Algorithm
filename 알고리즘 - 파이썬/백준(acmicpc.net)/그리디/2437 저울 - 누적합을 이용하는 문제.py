import sys
# input = sys.stdin.readline

n = int(input().rstrip())
weight = list(map(int, input().rstrip().split()))

weight.sort()

ans = 0
for i in weight:
    if ans+1 < i:
        break
    ans += i
print(ans + 1)
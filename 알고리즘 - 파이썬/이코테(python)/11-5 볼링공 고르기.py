from itertools import permutations
import sys
# input = sys.stdin.readline

# 2개?

n, m = map(int, input().rstrip().split())
ball = list(map(int, input().rstrip().split()))

ball.sort()

permute = list(permutations(ball, 2))
ans = 0

for x in permute:
    if x[0] != x[1]:
        ans += 1

print(ans // 2)    





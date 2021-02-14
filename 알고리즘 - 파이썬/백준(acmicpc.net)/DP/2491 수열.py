import sys
# input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
dp1 = [0 for _ in range(n)] # 0 ~ n-1
dp2 = [0 for _ in range(n)] # 0 ~ n-1

dp1[0] = 1
for i in range(1, n):
    if a[i] >= a[i-1]:
        dp1[i] = dp1[i-1] + 1
    else:
        dp1[i] = 1

max_dp1 = max(dp1)

dp2[0] = 1
for i in range(1, n):
    if a[i] <= a[i-1]:
        dp2[i] = dp2[i-1] + 1
    else:
        dp2[i] = 1

max_dp2 = max(dp2)

print(max(max_dp1, max_dp2))
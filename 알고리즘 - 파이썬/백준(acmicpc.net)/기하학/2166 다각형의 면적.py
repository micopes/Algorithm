import sys
# input = sys.stdin.readline

n = int(input().rstrip())

point = []

for i in range(n):
    x, y = map(int, input().rstrip().split())
    point.append([x, y])

point.append(point[0])

sum1 = 0
sum2 = 0

for i in range(n):
    sum1 += point[i][0] * point[i+1][1]
    sum2 += point[i][1] * point[i+1][0]

ans = round((sum1-sum2)/2, 1)
if ans < 0:
    ans *= -1

print(ans)


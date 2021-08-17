import sys
# input = sys.stdin.readline

n = int(input().rstrip())

data = list(map(int, input().rstrip().split()))

data.sort()

cnt = 0 # 현재 그룹의 인원
ans = 0

for i in range(n):
    cnt += 1
    if cnt >= data[i]:
        cnt = 0
        ans += 1

print(ans)

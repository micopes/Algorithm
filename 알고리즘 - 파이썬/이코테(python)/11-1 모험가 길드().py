import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = list(map(int, input().rstrip().split()))

data.sort()

result = 0 # 그룹 수
cnt = 0 # 현재 그룹에 포함된 사람 수

for i in data:
    cnt += 1
    if cnt >= i:
        cnt = 0
        result += 1

print(result)



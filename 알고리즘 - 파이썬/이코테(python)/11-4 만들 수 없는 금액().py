import sys
# input = sys.stdin.readline

n = int(input().rstrip())

coin = list(map(int, input().rstrip().split()))
coin.sort()

target = 1
for x in coin:
    if target < x:
        break

    target += x

print(target)
        



# 해설 : https://aerocode.net/392
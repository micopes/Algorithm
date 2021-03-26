import sys
# input = sys.stdin.readline

n = int(input().rstrip())
nList = list(map(int, input().rstrip().split()))

m = int(input().rstrip())
mList = list(map(int, input().rstrip().split()))

existNum = [0 for _ in range(1000001)]

for x in nList:
    existNum[x] = 1

for y in mList:
    if existNum[y] == 1:
        print("yes")
    else:
        print("no")
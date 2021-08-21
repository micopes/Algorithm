import sys
# input = sys.stdin.readline

n = int(input().rstrip())
li = []

for i in range(n):
    temp = list(input().rstrip().split())
    temp[0] = str(temp[0])
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    temp[3] = int(temp[3])
    li.append(temp)

li.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(li[i][0])

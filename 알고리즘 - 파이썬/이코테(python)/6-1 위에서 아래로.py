import sys
# input = sys.stdin.readline

n = int(input().rstrip())

data = []
for i in range(n):
    x = int(input().rstrip())
    data.append(x)

data.sort(reverse = True)
for i in data:
    print(i, end = " ")
    
import sys

n = int(sys.stdin.readline())

data = [[0]*2 for _ in range(n)] # [n-1][0], [n-1][1]

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data[i][0] = x
    data[i][1] = y

data.sort()

for i in range(n):
    print("%d %d" % (data[i][0], data[i][1]))
    
    
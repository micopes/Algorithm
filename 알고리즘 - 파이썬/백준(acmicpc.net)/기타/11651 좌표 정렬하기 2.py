n = int(input())

data = [[0]*2 for _ in range(n)] # [n-1][0], [n-1][1]

for i in range(n):
    x, y = map(int, input().split())
    data[i][0] = y
    data[i][1] = x

data.sort()

for i in range(n):
    print("%d %d" % (data[i][1], data[i][0]))
    
    
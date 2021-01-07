n = int(input())

data = [[0]*4 for _ in range(100000)] # [99999][0] [99999][1] [99999][2] [99999][3] 

for i in range(n):
    data[i] = list(input().split())
    # [i][0]은 그대로
    data[i][1] = int(data[i][1])
    data[i][2] = int(data[i][2])
    data[i][3] = int(data[i][3])

data = sorted(data, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print("%s" % (data[i][0]))
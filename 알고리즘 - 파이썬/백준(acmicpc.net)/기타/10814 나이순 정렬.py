n = int(input())

# 숫자가 같으면 정렬하지 않고 숫자가 다를때만 정렬한다.
data = [[0]*2 for _ in range(n)] # [0 ~ 99999][0], [1]

for i in range(n):
    x, y = input().split()
    x = int(x)
    data[i][0] = x
    data[i][1] = y

data = sorted(data, key = lambda x : x[0])

for i in range(n):
    print("%d %s" % (data[i][0], data[i][1]))

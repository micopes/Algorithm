n = int(input())
data = sorted(map(int, input().split()))
dic = {}
for i in data:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

m = int(input())
data2 = map(int, input().split())

for i in data2:
    if i in dic:
        print(dic[i], end = " ")
    else:
        print(0, end = " " )
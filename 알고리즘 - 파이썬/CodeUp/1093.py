n = int(input())
num = list(map(int, input().split()))

data = []
for i in range(24) :
    data.append(0)
    
for k in num :
    data[k] += 1

for i in range(1, 24):
    print(data[i], end = " ")
    

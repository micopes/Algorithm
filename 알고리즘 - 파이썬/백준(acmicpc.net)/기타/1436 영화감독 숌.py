n = int(input())

data = [0] # [0] = 0
for i in range(10000000):
    if "666" in str(i):
        data.append(i)

print(data[n])
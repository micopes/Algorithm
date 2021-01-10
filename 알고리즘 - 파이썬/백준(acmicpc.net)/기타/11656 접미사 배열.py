string = input()

data = []
for i in range(len(string)):
    data.append(string[i::])

data.sort()

for i in range(len(data)):
    print(data[i])
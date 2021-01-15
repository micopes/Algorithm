data = []
n = int(input())

for i in range(n):
    string = input()
    if string not in data:
        data.append(string)

data = sorted(data, key = lambda x : (len(x), x))

for x in data:
    print(x)
n = int(input())

data = []
for i in range(n):
    x = int(input())
    data.append(x)
    
data.sort()
for item in data:
    print(item)
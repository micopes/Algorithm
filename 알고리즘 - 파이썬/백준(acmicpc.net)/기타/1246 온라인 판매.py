import sys
# input = sys.stdin.readline

egg, n = map(int, input().strip().split())

data = []
for i in range(n):
    x = int(input().strip())
    data.append(x)

data.sort()

result = 0
price = -1
for i in range(len(data)):
    temp = data[i] * min(egg, len(data)-i)
    if result < temp:
        result = temp
        price = data[i]

print(price, result)
    
    
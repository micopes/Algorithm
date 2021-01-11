n = int(input())
result = 0
for i in range(1, n+1):
    if i % 125 == 0:
        result += 3
    elif i % 25 == 0:
        result += 2
    elif i % 5 == 0:
        result += 1

print(result)
        
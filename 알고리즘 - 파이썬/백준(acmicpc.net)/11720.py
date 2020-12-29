n = int(input())

k = int(input())

result = 0
for i in range(n):
    result += (k % 10)
    k //= 10

print(result)
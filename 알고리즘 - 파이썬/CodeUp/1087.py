n = int(input())

num = 1
result = 0
while True :
    result += num
    num += 1
    if result >= n:
        break
print(result)
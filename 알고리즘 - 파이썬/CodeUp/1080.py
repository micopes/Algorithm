n = int(input())
result = 0

num = 0
for i in range(1, 100):
    result += num
    if(result >= n):
        print(num)
        break
    num += 1



    
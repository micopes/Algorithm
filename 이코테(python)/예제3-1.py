# 예제 3-1 거스름돈

N = int(input())

coin = [500, 100, 50, 10]

count = 0
for i in coin :
    count += (N // i)
    N %= i

print(count)
    
    
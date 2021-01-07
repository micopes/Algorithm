def hanoi(n, start, temp, end):
    if n == 1:
        print("%c %c" % (start, end))
    else :
        hanoi(n-1, start, end, temp)
        print("%c %c" % (start, end))
        hanoi(n-1, temp, start, end)

n = int(input())
num = 0

for i in range(n):
    num = num * 2 + 1

print(num)
hanoi(n, '1', '2', '3')




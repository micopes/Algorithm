import sys
input = sys.stdin.readline

index = int(input().rstrip())
# x / y
x, y = 1, 1
result = []
for i in range(1000):
    result.append([x, y])
    if x == 1:
        x = y+1
        y = 1
    else:
        x -= 1
        y += 1

print(result[index-1][0], result[index-1][1])
    
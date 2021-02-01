import sys
# input = sys.stdin.readline

x, y = input().split()

x = x[::-1]
y = y[::-1]
result = str(int(x) + int(y))
result = result[::-1]
print(int(result))
    
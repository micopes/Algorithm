import sys
# input = sys.stdin.readline

n = int(input())
result = n//5
if n % 5 != 0:
    result += 1
print(result)
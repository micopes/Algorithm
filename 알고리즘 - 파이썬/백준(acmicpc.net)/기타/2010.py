import sys
input = sys.stdin.readline

n = int(input().strip())

result = 0
result += int(input())
for i in range(1, n):
    result += (int(input()) -1)

print(result)
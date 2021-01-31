import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input().strip())
numbers = list(map(int, input().strip().split()))
    
result = -1
for p in permutations(numbers, n):
    temp = 0
    for i in range(0, len(p)-1):
        temp += abs(p[i] - p[i+1])
    result = max(result, temp)
print(result)
        
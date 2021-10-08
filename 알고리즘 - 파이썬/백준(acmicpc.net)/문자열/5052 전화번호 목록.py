import sys
# input = sys.stdin.readline

def solve(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] == numbers[i+1][0:len(numbers[i])]:
            return "NO"
    
    return "YES"

T = int(input())

for _ in range(T):
    n = int(input().rstrip())
    
    numbers = []
    for i in range(n):
        numbers.append(input().rstrip())
    numbers.sort()
    
    print(solve(numbers))
        
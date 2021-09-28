import sys
# input = sys.stdin.readline

N, M = map(int, input().rstrip().split())


numbers = [0]
numbers.extend(list(map(int, input().rstrip().split())))

for i in range(len(numbers)):
    numbers[i] += numbers[i-1]

for i in range(M):
    start, end = map(int, input().rstrip().split())
    print(numbers[end] - numbers[start-1])
    


    
    
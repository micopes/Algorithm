import sys
# input = sys.stdin.readline

numbers = [-1]

for i in range(1, 21):
    numbers.append(i)

for i in range(10):
    start, end = map(int, input().rstrip().split()) # 둘다 포함
    for j in range(start, (start + end) // 2 + 1):
        numbers[j], numbers[start+end-j] = numbers[start+end-j], numbers[j]
    
for i in range(1, 21):
    print(numbers[i], end = " ")
        
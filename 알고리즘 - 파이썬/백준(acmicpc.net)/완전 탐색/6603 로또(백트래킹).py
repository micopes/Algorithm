import sys
input = sys.stdin.readline

def printOutput(numbers):
    for i in numbers:
        print(i, end = " ")
    print()
            

def backtrack(idx, numbers):
    if len(numbers) == 6:
        printOutput(numbers)
        return
    
    if idx < len(data):
        # data[idx]를 포함하는
        numbers.append(data[idx])
        backtrack(idx+1, numbers)
        numbers.pop()
        
        # data[idx]를 포함하지 않는 
        backtrack(idx+1, numbers)
        
while True:
    temp = list(map(int ,input().rstrip().split()))
    n = temp[0]
    if n == 0:
        break
    data = temp[1:]
    
    backtrack(0, [])
    print()

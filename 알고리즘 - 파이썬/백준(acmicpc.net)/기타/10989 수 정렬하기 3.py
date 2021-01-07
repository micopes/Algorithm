import sys

n = int(sys.stdin.readline()) # sys.stdin.readline()

data = [0 for _ in range(10001)] # 1 ~ 10000

for i in range(n):
    x = int(sys.stdin.readline())
    data[x] += 1
    
for i in range(1, 10001):
    for j in range(data[i]):
        print(i)
        
    
import sys
# input = sys.stdin.readline

n = int(input().rstrip())

data = []
for i in range(n):
    name, score = input().rstrip().split()
    score = int(score)
    data.append([name, score])

data.sort(key = lambda x : x[1])

for i in range(len(data)):
    print(data[i][0], end = " ")
    
    



import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

num = [0, 0, 0] # 0, 1, -1(2) 각각.

def isValid(x, y, n):
    k = data[x][y]
    if n == 1:
        num[k] += 1
        return
    
    flag = True
    for i in range(x, x+n):
        for j in range(y, y+n):
            if data[i][j] != k:
                flag = False
                break
        if flag == False:
            break
    
    if flag == True:
        num[k] += 1
    else:
        step = n // 3
        for i in range(x, x+n, step):
            for j in range(y, y+n, step):
                isValid(i, j, step)
            
n = int(input().strip())

data = []

for i in range(n):
    temp = list(map(int, input().strip().split()))
    data.append(temp)
    
isValid(0, 0, n)
for i in [-1, 0, 1]:
	print(num[i])
    

import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def quadTree(x, y, n):
    k = data[x][y]
    if n == 1:
        print(k, end = "")
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
        print(k, end = "")
    else:
        step = n // 2
        for i in range(x, x+n, step):
            for j in range(y, y+n, step):
                print('(', end = "")
                quadTree(i, j, step)
                print(')', end = "")
    

n = int(input().strip())

data = []
for i in range(n):
    string = input().strip()
    data.append(string)
print('(', end = "")
quadTree(0, 0, n)
print(')', end = "")

    
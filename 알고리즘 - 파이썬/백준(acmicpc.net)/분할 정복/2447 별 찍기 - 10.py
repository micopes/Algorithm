import sys
# input = sys.stdin.readline
sys.setrecursionlimit(111111)

def starBox(x, y, n):
    if n == 1:
        empty = 1
        if x == empty and y == empty:
            pass
        else:
            data[x][y] = '*'
        return
    
    step = n // 3
    for i in range(x, x+n, step):
        for j in range(y, y+n, step):
            if i == x+step and j == y+step:
                pass
            else:
                starBox(i, j, step)
            

n = int(input().strip())
data = [[' ']*n for _ in range(n)]
starBox(0, 0, n)

for i in range(n):
    for j in range(n):
        print(data[i][j], end = "")
    print()


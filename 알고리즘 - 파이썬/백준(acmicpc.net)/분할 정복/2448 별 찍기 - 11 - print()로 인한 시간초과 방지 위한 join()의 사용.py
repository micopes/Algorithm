import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

n = int(input())
data = [[' ']*(2*n-1) for _ in range(n)]

def starTriangle(y, x, n):
    if n == 3:
        data[y][x] = '*'
        data[y+1][x-1] = data[y+1][x+1] = '*'
        data[y+2][x-2] = data[y+2][x-1] =\
            data[y+2][x] = data[y+2][x+1] = data[y+2][x+2] =\
                '*'
    else:
        step = n // 2
        starTriangle(y, x, step)
        starTriangle(y+step, x-step, step)
        starTriangle(y+step, x+step, step)

starTriangle(0, n-1, n)
for i in range(n):
    print("".join(data[i]))
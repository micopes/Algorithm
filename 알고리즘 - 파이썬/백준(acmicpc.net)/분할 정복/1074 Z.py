import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def recur(N, row, col):
    global r, c
    size = 2**(N-1)
    if N == 0:
        return 1
    
    if row < size:
        if col < size:
            return recur(N-1, row, col)
        else:
            return size*size + recur(N-1, row, col-size)
    else:
        if col < size:
            return size*size*2 + recur(N-1, row-size, col)
        else:
            return size*size*3 + recur(N-1, row-size, col-size)
        
N, r, c = map(int, input().rstrip().split())
print(recur(N, r, c)-1)

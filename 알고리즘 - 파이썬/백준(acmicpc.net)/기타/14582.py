import sys
# input = sys.stdin.readline

def solve(ulim, start):
    uT = 0
    sT = 0
    for i in range(9):
        uT += ulim[i]
        if uT > sT:
            return "Yes"
        sT += start[i]
    
    return "No"
            
ulim = list(map(int, input().rstrip().split()))
start = list(map(int, input().rstrip().split()))

print(solve(ulim, start))

    
    
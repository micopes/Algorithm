import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    temp = list(map(int, input().rstrip().split()))
    
    n = temp[0]
    if n == 0:
        break
    numbers = temp[1:]
    
    nCr = combinations(numbers, 6)
    nCr = list(nCr)
    for i in range(len(nCr)):
        for j in nCr[i]:
            print(j, end = " ")
        print()
    print()


import sys
from itertools import permutations
# input = sys.stdin.readline
    
n = int(input().strip())
table = [list(map(int, input().strip().split())) for _ in range(n)]

result = sys.maxsize
city = [i for i in range(n)]
for p in permutations(city, n):
    val = 0
    flag = True
    for i in range(len(p)-1):
        if table[p[i]][p[i+1]] == 0:
            flag = False
            break
        val += table[p[i]][p[i+1]]
        
    if table[p[-1]][p[0]] == 0:
        flag = False
    val += table[p[-1]][p[0]]
    
    if flag == True:
        result = min(result, val)    
        
print(result)



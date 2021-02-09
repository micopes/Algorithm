import sys
# input = sys.stdin.readline


n, m = map(int, input().rstrip().split())
poke = {} 
for i in range(1, n+1):
    string = input().rstrip()
    idx = str(i)
    poke[idx] = string
    poke[string] = i
    
for i in range(m):
    inp = input().strip()
    print(poke[inp])
    
    
    
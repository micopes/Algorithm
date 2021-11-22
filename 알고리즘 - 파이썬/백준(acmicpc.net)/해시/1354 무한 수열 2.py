import sys
# input = sys.stdin.readline

def dfs(n):
    if n in dic:
        return dic[n]
    
    # else
    key = n//p-x
    if key <= 0:
        dic[key] = 1
        
    key2 = n//q-y
    if key2 <= 0:
        dic[key2] = 1
        
    dic[n] = dfs(key) + dfs(key2)
    return dic[n]

n, p, q, x, y = map(int, input().rstrip().split())

dic = {}
dic[0] = 1

print(dfs(n))

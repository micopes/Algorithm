import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

def dfs(data, visited, result, cycle, x):
    visited[x] = 1
    cycle.append(x)
    
    for val in data[x]:
        if visited[val] == 0:
            dfs(data, visited, result, cycle, val)
        else: # visited[val] == 1
            if val in cycle:
                for i in range(cycle.index(val), len(cycle)):
                    result[cycle[i]] = 1
            return

T = int(input())

for l in range(T):
    n = int(input())
    _list = [0] + list(map(int, input().split())) # 0 ~ n-1
    visited = [0 for _ in range(n+1)]
    data = [[] for _ in range(n+1)]
    result = [0 for _ in range(n+1)]
    
    for i in range(1, n+1): # 1 ~ n
        if i == _list[i]:
            result[i] = 1
        else:
            data[i].append(_list[i])
    
    for i in range(1, n+1):
        if visited[i] == 0:
            cycle = []
            dfs(data, visited, result, cycle, i)
            
    count = 0
    for i in range(1, len(result)):
        if result[i] == 0:
            count += 1
    print(count)
    
    
            
    
            
        
        
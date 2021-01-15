T= int(input())

def dfs(data, visited, n):
    visited[n] = 1
    for val in data[n]:
        if visited[val] == 0:
            dfs(data, visited, val)

for l in range(T):
    n = int(input())
    visited = [0 for _ in range(n+1)] # 1 ~ n
    data = [[] for _ in range(n+1)] # 1 ~ n
    
    _list = list(map(int, input().split()))
    for i in range(1, n+1):
        data[i].append(_list[i-1])
        data[_list[i-1]].append(i)
    
    count = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            dfs(data, visited, i)
            count += 1
    print(count)
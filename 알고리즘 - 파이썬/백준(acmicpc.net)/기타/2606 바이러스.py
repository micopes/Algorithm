import sys
# input = sys.stdin.readline

def dfs(computer):
    visited[computer] = 1
    for i in corr[computer]:
        if visited[i] == 0:
            dfs(i)
    

n = int(input().rstrip())
m = int(input().rstrip())

corr = [[] for _ in range(n+1)] # 1 ~ n
visited = [0 for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().rstrip().split())
    corr[x].append(y)
    corr[y].append(x)

dfs(1)
result = 0
for i in range(2, n+1): # 2 ~ n
    if visited[i] == 1:
        result += 1

print(result)
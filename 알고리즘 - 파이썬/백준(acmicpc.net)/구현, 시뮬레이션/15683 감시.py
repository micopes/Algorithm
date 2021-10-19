import sys
import copy
# input = sys.stdin.readline

# [0, 1, 2, 3] : 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [1, 3], [1, 2], [0, 2]],
    [[0, 2, 3], [0, 1, 3], [0, 1, 2], [1, 2, 3]],
    [[0, 1, 2, 3]]    
]

def count_num(graph):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

def dfs(graph, depth):
    global ans
    if depth == len(cctv):
        ans = min(ans, count_num(graph))
        return
        
    temp = copy.deepcopy(graph)
    
    x, y, cctv_type = cctv[depth]
    
    for di in directions[cctv_type]:
        watch(temp, x, y, di)
        dfs(temp, depth+1)
        temp = copy.deepcopy(graph)
        
def watch(graph, x, y, di):
    for d in di:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 6:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = '#'
                # 벽이 있는 경우 종료
                else:
                    break
            # 범위 밖을 벗어나는 경우 종료
            else:
                break
            
n, m = map(int, input().rstrip().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

cctv = []
ans = 0
for i in range(n):
    for j in range(m):
        if 1 <= graph[i][j] <= 5:
            cctv.append([i, j, graph[i][j]])
        elif graph[i][j] == 0:
            ans += 1

dfs(graph, 0)
print(ans)
            


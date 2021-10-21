import sys
# input = sys.stdin.readline
sys.setrecursionlimit(111111)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(picked, S, Y):
    global answer
    if Y > 3:
        return
    
    if S + Y == 7 and S >= 4:
        picked = tuple(sorted(picked))
        if picked not in visited:
            visited.add(picked)
            answer += 1
        return
    
    for pos in picked:
        x = pos // 5
        y = pos % 5
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            n = nx*5 + ny
            if 0 <= nx < 5 and 0 <= ny < 5 and n not in picked:
                picked.append(n)
                if graph[nx][ny] == 'S':
                    dfs(picked, S+1, Y)
                else:
                    dfs(picked, S, Y+1)
                picked.pop()

    
graph = []
for _ in range(5):
    graph.append(list(input().rstrip()))

visited = set()
answer = 0


for i in range(5):
    for j in range(5):
        if graph[i][j] == 'S':
            picked = []
            picked.append(i*5+j)
            dfs(picked, 1, 0)
            
print(answer)

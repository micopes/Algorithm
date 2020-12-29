n = int(input())
x, y = 1, 1
di = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
types = ['L', 'R', 'U', 'D']

for d in di :
    for i in range(len(types)):
        if d == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx > n or nx < 1 or ny > n or ny < 1:
        continue
    x, y = nx, ny
    
print(x, y)
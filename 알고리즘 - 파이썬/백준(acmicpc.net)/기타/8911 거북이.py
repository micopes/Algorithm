import sys
# input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input().rstrip())
for _ in range(n):
    box = [[0]*1001 for _ in range(1001)]
    
    di = 0 # 위를 바라보고 있다.
    X, Y = 500, 500 # 현재 위치
    box[500][500] = 1
    string = input().rstrip()
    
    maxX = 500
    minX = 500
    maxY = 500
    minY = 500
    
    for ch in string:
        if ch == 'F':
            X += dx[di]
            Y += dy[di]
            box[X][Y] = 1
        elif ch == 'B':
            X -= dx[di]
            Y -= dy[di]
            box[X][Y] = 1
        elif ch == 'R':
            di += 1
            di %= 4
        elif ch == 'L':
            di -= 1
            di %= 4
        maxX = max(X, maxX)
        maxY = max(Y, maxY)
        minX = min(X, minX)
        minY = min(Y, minY)
        
    print((maxX-minX)*(maxY-minY))
    
                

            
        
    

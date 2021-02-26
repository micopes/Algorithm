import sys
# input = sys.stdin.readline

def recur(x, y, n):
    global white, blue
    if n == 1:
        if board[x][y] == 0:
            white += 1
        else:
            blue += 1
        return
    
    flag = True
    prev = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if prev != board[i][j]:
                flag = False
    
    nextN = n//2
    if flag == False:
        recur(x, y, nextN)
        recur(x+nextN, y, nextN)
        recur(x, y+nextN, nextN)
        recur(x+nextN, y+nextN, nextN)
    else:
        if board[x][y] == 0:
            white += 1
        else:
            blue += 1
        return
            
    

n = int(input().rstrip())

board = []
white, blue = 0, 0 # 0 : white, 1 : blue
for i in range(n):
    temp = list(map(int, input().rstrip().split()))
    board.append(temp)
    
recur(0, 0, n)

print(white)
print(blue)
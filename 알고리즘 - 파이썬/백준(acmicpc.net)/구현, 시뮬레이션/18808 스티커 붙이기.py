import sys
# input = sys.stdin.readline

def check_sticker(sticker, x, y):
    r, c = len(sticker), len(sticker[0])
    
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and board[x+i][y+j] == 1:
                return False
    
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                board[x+i][y+j] = 1
    
    return True

def rotate_sticker(sticker):
    c, r = len(sticker), len(sticker[0])
    
    temp = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            temp[i][j] = sticker[c-1-j][i]
    
    return temp

ROW, COL, K = map(int, input().rstrip().split())
board = [[0]*COL for _ in range(ROW)]

stickers = []
for _ in range(K):
    r, c = map(int, input().rstrip().split())
    temp = []
    for i in range(r):
        temp.append(list(map(int, input().rstrip().split())))
    stickers.append(temp)

for sticker in stickers:
    turn = 1
    while True:
        r, c = len(sticker), len(sticker[0])
        flag = False
        for x in range(ROW-(r-1)):
            for y in range(COL-(c-1)):
                if check_sticker(sticker, x, y) == True:
                    flag = True
                    break
            if flag == True:
                break
        
        if flag == True:
            break
        else:
            if turn == 0:
                break
            turn = (turn + 1) % 4
            sticker = rotate_sticker(sticker)
        

ans = 0
for i in range(ROW):
    for j in range(COL):
        if board[i][j] == 1:
            ans += 1

print(ans)
            
                    
    
        
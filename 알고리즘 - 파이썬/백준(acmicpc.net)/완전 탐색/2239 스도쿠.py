import sys
input = sys.stdin.readline

def printOutput():
    for i in range(9):
        for j in range(9):
            print(block[i][j], end = "")
        print()
        
def promising(x, y):
    poss = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    imposs = set()
    
    for i in range(9):
        imposs.add(block[x][i])
        imposs.add(block[i][y])
    
    tempX = x // 3 * 3
    tempY = y // 3 * 3
    for i in range(tempX, tempX + 3):
        for j in range(tempY, tempY + 3):
            imposs.add(block[i][j])
    
    poss = list(poss - imposs)
    return poss

def backtrack(idx):
    global flag
    if flag == True:
        return 
    
    if idx == len(blank):
        flag = True
        printOutput()
        return 
    
    x = blank[idx][0]
    y = blank[idx][1]
    
    poss = promising(x, y)
    
    for i in poss:
        block[x][y] = i
        backtrack(idx + 1)
        block[x][y] = 0
    
    


block = []
blank = []
for i in range(9):
    block.append(list(input().rstrip()))
    
for i in range(9):
    for j in range(9):
        block[i][j] = int(block[i][j])

for i in range(9):
    for j in range(9):
        if block[i][j] == 0:
            blank.append([i, j])
    
flag = False
backtrack(0)
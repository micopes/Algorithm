import sys
# input = sys.stdin.readline

def printResult():
    for i in range(9):
        for j in range(9):
            print(block[i][j], end = " ")
        print()
def promising(x, y):
    poss = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    imposs = set()
    
    for i in range(9):
        imposs.add(block[x][i])
        imposs.add(block[i][y])
    tempX = x // 3 * 3
    tempY = y // 3 * 3
    for i in range(tempX, tempX+3):
        for j in range(tempY, tempY+3):
            imposs.add(block[i][j])
    ret = list(poss - imposs)
    return ret


def backtrack(idx):
    global flag
    if flag == True:
        return
    
    if idx == len(blank):
        flag = True
        printResult()
        return

    x = blank[idx][0]
    y = blank[idx][1]
    
    poss = promising(x, y)
    
    for i in poss:
        block[x][y] = i
        backtrack(idx+1)
        block[x][y] = 0

block = []
blank = []

for i in range(9):
    block.append(list(map(int, input().rstrip().split())))
flag = False
for i in range(9):
    for j in range(9):
        if block[i][j] == 0:
            blank.append([i, j])

backtrack(0) # x, y = blank[0][0], blank[0][1], block[x][y] = 0




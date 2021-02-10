import sys
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

board = []
for i in range(n):
    board.append(list(input().rstrip()))

result = sys.maxsize
for maxI in range(n - 7):
    for maxJ in range(m - 7):
        min_val = 0
        min_val2 = 0
        for i in range(maxI, maxI+8):
            for j in range(maxJ, maxJ+8):
                if (i + j) % 2 == 0 and board[i][j] != 'W':
                    min_val += 1
                elif (i + j) % 2 == 1 and board[i][j] != 'B':
                    min_val += 1
                
                if (i + j) % 2 == 0 and board[i][j] != 'B':
                    min_val2 += 1
                elif (i + j) % 2 == 1 and board[i][j] != 'W':
                    min_val2 += 1
        temp = min(min_val, min_val2)
        if result > temp:
            result = temp

print(result)
            
            
    
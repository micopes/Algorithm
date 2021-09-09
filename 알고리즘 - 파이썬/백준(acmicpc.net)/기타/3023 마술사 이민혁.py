import sys
# input = sys.stdin.readline

# 입력
R, C = map(int, input().rstrip().split())

card = []

for i in range(R):
    string = input()
    card.append(list(string))
    
x, y = map(int, input().rstrip().split())

# 오른쪽 위
for i in range(R):
    for j in range(C, 2*C):
        card[i].append(card[i][2*C-1-j])

# 왼쪽 아래
for i in range(R, 2*R):
    card.append([])
    for j in range(C):
        card[i].append(card[2*R-1-i][j])
    
# 오른쪽 아래
for i in range(R, 2*R):
    for j in range(C, 2*C):
        card[i].append(card[2*R-1-i][2*C-1-j])

if card[x-1][y-1] == '.':
    card[x-1][y-1] = '#'
elif card[x-1][y-1] == '#':
    card[x-1][y-1] = '.'

# 출력
for i in range(2*R):
    for j in range(2*C):
        print(card[i][j], end = "")
    print()
    
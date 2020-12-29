h, w = map(int, input().split()) # 가로, 세로
n = int(input()) # 놓을 수 있는 막대의 개수
# l, d, x, y = int(input())
# d : 막대를 놓는 방향 가로 : 0, 세로 : 1

data = [[0]*w for i in range(h)]

for i in range(n) :
    l, d, x, y = map(int, input().split())
    # 좌표값에 따른 위치 조정
    x -= 1
    y -= 1
    for j in range(l):
        if d == 0:
            data[x][y+j] = 1
        else:
            data[x+j][y] = 1

for i in range(h) :
    for j in range(w) :
        print(data[i][j], end = " ")
    print()
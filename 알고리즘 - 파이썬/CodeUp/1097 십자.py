zeros = []

for i in range(19) :
    data = list(map(int, input().split()))
    zeros.append(data)

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    # 위치 조정
    x = x-1
    y = y-1
    for j in range(19):
        if zeros[x][j] == 1:
            zeros[x][j] = 0
        else :
            zeros[x][j] = 1
        
        if zeros[j][y] == 1:
            zeros[j][y] = 0
        else:
            zeros[j][y] = 1
        

for i in range(19):
    for j in range(19):
        print(zeros[i][j], end = " ")
    print()
        

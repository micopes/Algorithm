# 오른쪽으로 움직이다가
# *벽을 만나면 
# 아래쪽으로(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다)

# 오른쪽으로 길 없으면 아래쪽으로.
# 목적지 도달 or 둘 다(오른쪽 and 아래쪽) 길 없으면 정지.

# (2, 2)에서 시작한다고 했으니 (1, 1)이라고 보면 될듯.

# 0 : 갈 수 있는 곳
# 1 : 갈 수 없는 곳
# 2 : 최종 목적지
# 간 경로는 9로 표시

# miro = [[0]*10 for i in range(10)]

miro = []

for i in range(10) :
    miro.append([])
    for j in range(10) :
        miro[i].append(0)
        
# 입력
for i in range(10):
    data = list(map(int, input().split()))
    for j in range(10):
        miro[j][i] = data[j]
        
# 프로세스
antX = 1
antY = 1

while True :
    if miro[antX][antY] == 2:
        miro[antX][antY] = 9
        break
    
    if antX + 1 == 10 or miro[antX+1][antY] == 1:
        if antY + 1 == 10 or miro[antX][antY+1] == 1:
            miro[antX][antY] = 9
            break            
        else:
            miro[antX][antY] = 9
            antY += 1
    else:
        miro[antX][antY] = 9
        antX += 1
        

for i in range(10):
    for j in range(10):
        print("%d" % (miro[j][i]), end = " ")
    print()

    
        
        

        



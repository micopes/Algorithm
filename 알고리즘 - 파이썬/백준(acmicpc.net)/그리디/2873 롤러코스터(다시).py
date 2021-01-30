import sys
# input = sys.stdin.readline


def findMin(box):
    indexX = -1
    indexY = -1
    minVal = 1000
    for i in range(0, m):
        for j in range(0, n):
            if (i+j) % 2 == 1 and minVal > box[i][j] :
                indexX = i
                indexY = j
                minVal = box[i][j]
                
    return indexX, indexY
            

# m : 세로, n : 가로
m, n = map(int, input().strip().split()) 

box = [] # [m][n]
            
for i in range(m):
    box.append(list(map(int, input().strip().split())))

visited = [[0]*n for _ in range(m)]

result = ""
if m % 2 == 1 and n % 2 == 1:
    cnt = 0
    end = m*n-1
    while True:
        for i in range(n-1):
            result += 'R'
            cnt += 1
        if cnt == end: 
            break
        result += 'D'
        cnt += 1
        for i in range(n-1):
            result += 'L'
            cnt += 1
        result += 'D'
        cnt += 1
elif m % 2 == 0 and n % 2 == 1:
    cnt = 0
    end = m*n-1
    while True:
        for i in range(m-1):
            result += 'D'
            cnt += 1
        if cnt == end:
            break
        result += 'R'
        cnt += 1
        for i in range(m-1):
            result += 'U'
            cnt += 1
        result += 'R'
        cnt += 1
elif m % 2 == 1 and n % 2 == 0:
    cnt = 0
    end = m*n-1
    while True:
        for i in range(n-1):
            result += 'R'
            cnt += 1
        if cnt == end:
            break
        result += 'D'
        cnt += 1
        for i in range(n-1):
            result += 'L'
            cnt += 1
        result += 'D'
        cnt += 1
else: # 짝수 x 짝수 2x2고려해줘야 하고, 
    # 방문하지 않을 점을 찾는다(검은 칸 중 최소점수)
    x, y = findMin(box)
    x1, y1, x2, y2 = 0, 0, m-1, n-1
    answer = ""
    subAnswer = ""
    while x2 - x1 > 1:
        if x1//2 < x//2:
            answer += 'R'*(n-1)
            answer += 'D'
            answer += 'L'*(n-1)
            answer += 'D'
            x1 += 2
        if x//2 < x2//2:
            subAnswer += 'R'*(n-1)
            subAnswer += 'D'
            subAnswer += 'L'*(n-1)
            subAnswer += 'D'
            x2 -= 2
    while y2 - y1 > 1:
        if y1//2 < y//2:
            answer += 'D'
            answer += 'R'
            answer += 'U'
            answer += 'R'
            y1 += 2
        if y//2 < y2//2:
            subAnswer += 'D'
            subAnswer += 'R'
            subAnswer += 'U'
            subAnswer += 'R'
            y2 -= 2
    
    if y == y1:
        answer += 'R'
        answer += 'D'
    else:
        answer += 'D'
        answer += 'R'
    
    answer += subAnswer[::-1]
    result += answer

print(result)
  
    

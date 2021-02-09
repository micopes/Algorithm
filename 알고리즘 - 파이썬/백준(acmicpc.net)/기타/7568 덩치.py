import sys
input = sys.stdin.readline

n = int(input().strip())

man = []
for i in range(n):
    x, y = map(int, input().rstrip().split())
    man.append([x, y])

for i in range(n):
    cnt = 1
    myX, myY = man[i][0], man[i][1]
    
    for j in range(n):
        if man[j][0] > myX and man[j][1] > myY:
            cnt += 1
    print(cnt, end = " ")
        
        
    
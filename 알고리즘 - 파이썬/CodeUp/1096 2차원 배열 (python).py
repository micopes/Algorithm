zeros = [[0]*19 for i in range(19)]

'''
# 이런 식으로도 가능함.
for i in range(20) :
    m.append([])
    for j in range(20) :
        m[i].append(0)
''' 

n = int(input())

for i in range(n) :
    x, y = map(int, input().split())
    zeros[x-1][y-1] = 1

for i in range(19) :
    for j in range(19) :
        print(zeros[i][j], end = " ")
    print()
    
    
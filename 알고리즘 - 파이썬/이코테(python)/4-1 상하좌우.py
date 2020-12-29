# 예제 4-1 상하좌우

n = int(input())
data = input().split()

x, y = 0, 0
for i in range(len(data)):
    if data[i] == 'L':
        if y == 0:
            pass
        else:
            y -= 1
    elif data[i] == 'R':
        if y == n-1:
            pass
        else:
            y += 1
    elif data[i] == 'U':
        if x == 0:
            pass
        else:
            x -= 1
    elif data[i] == 'D':
        if x == n-1:
            pass
        else:
            x += 1

# 0 ~ 4이기 때문에 1 ~ 5의 좌표를 표현해주기 위해서는 x+1, y+1이 필요            
print("%d %d" % (x+1, y+1))


        


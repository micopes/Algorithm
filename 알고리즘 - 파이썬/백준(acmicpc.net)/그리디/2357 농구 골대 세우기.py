import sys
# input = sys.stdin.readline

n = int(input().rstrip()) # 농구를 좋아하는 마을의 개수

x_list = []
y_list = [] 

for i in range(n):
    temp_x, temp_y, weight = map(int, input().rstrip().split())
    
    for _ in range(weight):
        x_list.append(temp_x)
        y_list.append(temp_y)


x_list.sort()
y_list.sort()

l = len(x_list)

if l % 2 == 0:
    print(x_list[l//2-1], y_list[l//2-1])
else:
    print(x_list[l//2], y_list[l//2])
    

    
    
import sys
# input = sys.stdin.readline

n = int(input().rstrip())

x_list = []
y_list = []
for i in range(n):
    x, y = map(int, input().rstrip().split())
    x_list.append(x)
    y_list.append(y)

x_list.sort()
y_list.sort()


# 최소가 되는 지점
min_x, min_y = -1, -1

if n % 2 == 0:
    min_x = x_list[n//2-1]
    min_y = y_list[n//2-1]
else:
    min_x = x_list[n//2]
    min_y = y_list[n//2]
    

ans = 0
for i in range(n):
    temp_x = abs(x_list[i] - min_x)
    temp_y = abs(y_list[i] - min_y)
    ans += temp_x
    ans += temp_y

print(ans)
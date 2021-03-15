import sys
# input = sys.stdin.readline

loc = input().rstrip()

w = ord(loc[0])-ord('a')
h = int(loc[1])-1

dx = [-1, -1, 1, 1, -2, -2, 2, 2]
dy = [-2, 2, -2, 2, -1, 1, -1, 1]

ans = 0
for i in range(8):
    tempX = w
    tempY = h
    nx = tempX + dx[i]
    ny = tempY + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        ans += 1

print(ans)

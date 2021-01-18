import math
import sys
input = sys.stdin.readline

def getDistance(mx, my, kx, ky):
    return math.sqrt((mx - kx)**2 + (my - ky)**2)

ax, ay, bx, by, cx, cy, dx, dy = map(int, input().strip().split())

interval = 1000000
mDx = (bx - ax) / interval
mDy = (by - ay) / interval
kDx = (dx - cx) / interval
kDy = (dy - cy) / interval

result = getDistance(ax, ay, cx, cy)
for i in range(1, interval+1):
    temp = getDistance(ax+mDx*i, ay+mDy*i, cx+kDx*i, cy+kDy*i)
    result = min(temp, result)
    
print(result)



import math
import sys
# input = sys.stdin.readline

def f(index): # distance
    return math.sqrt((mxList[index] - kxList[index])**2 + (myList[index] - kyList[index])**2)
   
ax, ay, bx, by, cx, cy, dx, dy = map(int, input().strip().split())

# m : 민호
# k : 강호

step1 = (bx-ax) / 1000000
start1 = ax
mxList = []
for i in range(1000000):
    mxList.append(start1)
    if start1 == bx:
        break
    start1 += step1
    
step2 = (by-ay) / 1000000
start2 = ay
myList = []
for i in range(1000000):
    myList.append(start2)
    if start2 == by:
        break
    start2 += step2

step3 = (dx-cx) / 1000000
start3 = cx
kxList = []
for i in range(1000000):
    kxList.append(start3)
    if start3 == dx:
        break
    start3 += step3
    
step4 = (dy-cy) / 1000000
start4 = cy
kyList = []
for i in range(1000000):
    kyList.append(start4)
    if start4 == dy:
        break
    start4 += step4    
    
start = 0
end = len(mxList)-1

p, q = 0, 0
while end - start >= 3:
    p = (start*2 + end) // 3
    q = (start + end*2) // 3
    if f(p) <= f(q):
        end = q
    else:
        start = p

result = 1000000
for i in range(1000000):
    result = min(result, f(i))

print(result)
    
    
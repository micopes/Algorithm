import sys
# input = sys.stdin.readline

while True:
    x1, x2, y1, y2 = map(int, input().strip().split())
    if x1 == x2 == y1 == y2 == 0:
        break
    print("%d %d" % (y1-x2, y2-x1))
    
    
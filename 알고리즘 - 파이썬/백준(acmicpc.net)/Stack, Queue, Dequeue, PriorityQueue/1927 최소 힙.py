import heapq
import sys
# input = sys.stdin.readline

n = int(input().rstrip())
heap = []
for i in range(n):
    x = int(input().rstrip())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
        
        
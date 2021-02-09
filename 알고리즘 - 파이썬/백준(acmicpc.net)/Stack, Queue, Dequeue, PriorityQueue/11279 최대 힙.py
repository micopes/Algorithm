import heapq
import sys
# input = sys.stdin.readline

heap = []
n = int(input().rstrip())
for i in range(n):
    x = int(input().rstrip())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            temp = heapq.heappop(heap)
            print(-temp)
    else:
        heapq.heappush(heap, -x)
        
# -val 을 넣는다.


import sys
import heapq
# input = sys.stdin.readline

n = int(input().rstrip())
heap = []

for i in range(n):
    card = int(input().rstrip())
    heapq.heappush(heap, card)

ans = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ans += (a+b)
    heapq.heappush(heap, a+b)
    

print(ans)    
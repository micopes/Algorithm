import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

score_list = list(map(int, input().rstrip().split()))

heap = []
for score in score_list:
    heapq.heappush(heap, -score)
    
for _ in range(k-1):
    heapq.heappop(heap)
    
print(-heapq.heappop(heap))
   

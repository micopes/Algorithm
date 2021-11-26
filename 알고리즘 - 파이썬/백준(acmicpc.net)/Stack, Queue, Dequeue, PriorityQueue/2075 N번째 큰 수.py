import sys
import heapq
# input = sys.stdin.readline

n = int(input().rstrip())

heap = []

for _ in range(n):
    nums = list(map(int, input().rstrip().split()))
    for num in nums:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)
    
print(heapq.heappop(heap))
    
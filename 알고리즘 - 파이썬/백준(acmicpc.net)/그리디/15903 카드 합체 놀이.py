import sys
import heapq
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

cards = list(map(int, input().rstrip().split()))
heapq.heapify(cards)

for i in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    
    heapq.heappush(cards, x+y)
    heapq.heappush(cards, x+y)
    
print(sum(cards))
    
import sys
import heapq
# input = sys.stdin.readline

n = int(input().rstrip())

heap = []
for _ in range(n):
    s, e = map(int, input().rstrip().split())
    heapq.heappush(heap, (s, e))

room = []
# 처음에 시작되는 방
s, e = heapq.heappop(heap)
# 종료 시간만 들어가면 기존의 heap과 비교하면서 가능
heapq.heappush(room, e)

while heap:
    s, e = heapq.heappop(heap)
    
    if s < room[0]:
        heapq.heappush(room, e)
    else:
        heapq.heappop(room)
        heapq.heappush(room, e)

print(len(room))
    
import sys
import heapq
# input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    k = int(input().rstrip())
    min_heap = []
    max_heap = []
    visited = [False] * 1000001
    for i in range(k):
        command, val = input().rstrip().split()
        val = int(val)
        if command == "I":
            heapq.heappush(min_heap, (val, i))
            heapq.heappush(max_heap, (-val, i))
            visited[i] = True
        elif command == "D":
            if val == 1:
                while max_heap and visited[max_heap[0][1]] == False:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and visited[min_heap[0][1]] == False:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    
    while max_heap and visited[max_heap[0][1]] == False:
        heapq.heappop(max_heap)
    while min_heap and visited[min_heap[0][1]] == False:
        heapq.heappop(min_heap)
    
    
    if len(min_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
                    
        
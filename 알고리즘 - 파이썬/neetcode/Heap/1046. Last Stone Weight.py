import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq, -stone) # -stone
        
        while len(pq) > 1:
            y = -heapq.heappop(pq)
            x = -heapq.heappop(pq)

            if x != y:
                heapq.heappush(pq, -(y-x))
                
        if len(pq) == 0:
            return 0
        else:
            return -pq[0]

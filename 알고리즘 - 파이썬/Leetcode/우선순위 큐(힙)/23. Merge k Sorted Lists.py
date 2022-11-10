import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        
        heap = []
        for key, val in dic.items():
            heapq.heappush(heap, (-val, key))
        
        result = []
        for _ in range(k):
            val, key = heapq.heappop(heap)
            result.append(key)
        
        return result

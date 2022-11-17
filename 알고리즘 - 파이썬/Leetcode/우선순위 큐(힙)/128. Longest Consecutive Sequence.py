import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = list(set(nums))
        heapq.heapify(nums)

        prev_val = -1000000000000
        max_length = 0
        if len(nums):
            max_length = 1
        length = 0

        while nums:
            x = heapq.heappop(nums)
            if prev_val + 1 == x:
                length += 1
            else:
                length = 1
            max_length = max(length, max_length)
            prev_val = x
        
        return max_length

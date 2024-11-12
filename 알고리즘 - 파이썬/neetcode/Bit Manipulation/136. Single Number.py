from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 1. 딕셔너리 사용 O(N)
        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1

        for num in nums:
            if dic[num] == 1:
                return num
        
        

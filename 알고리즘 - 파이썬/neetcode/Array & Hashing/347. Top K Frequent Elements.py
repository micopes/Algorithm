from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1

        tmp_list = []
        for key, val in num_dict.items():
            tmp_list.append((key, val)) # (num, cnt)
        
        tmp_list.sort(key = lambda x : -x[1]) # cnt 내림차순

        result = []
        for i in range(k):
            result.append(tmp_list[i][0])
        
        return result

        

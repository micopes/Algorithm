# 방법
# 1. 2중 for문 - 시간복잡도 O(N^2)
# 2. from itertools import combinations 이용해서 nC2 - 2중 for문과 같이 O(N^2)의 시간복잡도
# 3. dictionary 사용 - 동일한 수 있는 것 주의해야 한다. - 딕셔너리에 index 같이 저장할 수 있도록 해야 한다.
# 4. 투포인터 이용 - 정렬 이후에 사용해야 하므로 O(nlogn) 시간 소요, index를 추가해야 한다.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {} # key = nums[idx], val = idx
        for i in range(len(nums)):
            val = target - nums[i]
            if val in dic:
                return [dic[val], i]
            dic[nums[i]] = i
        
        
            
        
        
        

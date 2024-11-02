class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 딕셔너리 이용 탐색(O(1))을 이용한 O(N) 시간복잡도
        num_dic = dict() # key, value == val, idx
        for i in range(len(nums)):
            num_dic[nums[i]] = i # 동일한 키인 경우에는 이후에 저장된 것만 남음.

        for first_idx in range(len(nums)):
            temp_val = target - nums[first_idx]
            if temp_val in num_dic:
                second_idx = num_dic[temp_val]
                if first_idx < second_idx: # 동일한 것이 아니어야 함.
                    return [first_idx, second_idx]

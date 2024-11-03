# 방법
# 1. 삼중 for문 - 시간복잡도 문제
# 2. collections 이용 - 시간복잡도 문제 발생할 여지 충분함.
# 3. 투 포인터
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        result_dic = dict() # 리스트를 순회하지 않고도 해당 키가 존재하는 지를 확인하기 위함임. 키는 튜플
        nums.sort()

        for i in range(1, len(nums)-1):
            left_idx = 0
            right_idx = len(nums)-1
            while left_idx < i and i < right_idx:
                left_val = nums[left_idx]
                val = nums[i]
                right_val = nums[right_idx]

                three_val_sum = left_val + val + right_val
                if three_val_sum == 0:
                    # 이미 존재하는 것이 아닌 경우에만 추가.
                    if (left_val, val, right_val) not in result_dic:
                        result_dic[(left_val, val, right_val)] = 1 # 존재 여부 업데이트
                        result.append([left_val, val, right_val]) # 리스트 형태로 저장.
                    left_idx += 1
                    right_idx -= 1
                elif three_val_sum < 0:
                    left_idx += 1
                elif three_val_sum > 0:
                    right_idx -= 1

        return result

            



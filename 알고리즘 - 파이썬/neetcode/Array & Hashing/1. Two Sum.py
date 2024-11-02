class Solution:
    # 문제 조건
    # - 정확히 하나의 답만 있음.

    # 1. 이분 탐색
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(val, start, end):
            while start <= end:
                mid = (start + end) // 2
                if nums_list[mid][1] == val:
                    return mid
                elif nums_list[mid][1] < val:
                    start = mid + 1
                else:
                    end = mid - 1

            return -1

        nums_list = []
        for idx, val in enumerate(nums):
            nums_list.append((idx, val)) # (idx, val)

        # val 기준 오름차순으로 정렬
        nums_list.sort(key = lambda x: x[1])
        print(nums_list)

        for i in range(len(nums_list)):
            f_idx, f_val = nums_list[i][0], nums_list[i][1]
            # 다음 차례부터 끝까지 검사.
            j = binarySearch(target-f_val, i+1, len(nums)-1)
            if j > 0:
                s_idx = nums_list[j][0]
                return [f_idx, s_idx]


        

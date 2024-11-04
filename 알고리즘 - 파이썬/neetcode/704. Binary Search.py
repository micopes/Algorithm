class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums는 오름차순 정렬되어 있음
        # 타겟이 되는 수가 존재하면 index를 리턴하고,
        #              존재하지 않으면 -1을 리턴
        
        left = 0
        right = len(nums)-1

        # 크거나 같다로 해야 리스트 element가 하나인 경우를 커버할 수 있음.
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        
        return -1
        

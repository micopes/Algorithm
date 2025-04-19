import heapq
import sys

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 방법 ?
        # 1. 해시? 
        # 2. 정렬은 안되고 O(nlogn)이니까.
        # 3. O(n)이라는 건 한번 select할 때 뽑아야 된다는 건데. 아 뭐 두번해도 되기는 하지. 우선순위큐하면 되나 ? 우선순위큐에 넣은 다음에 연속되는거 있는지 한번 뽑아보면서 확인하면 되지. 
        #    - 이 때, 같은 숫자가 나왔다고 해도 그냥 넘어가야 함.
        pq = []
        for num in nums:
            heapq.heappush(pq, num)

        max_conseq = 0 # 최대 연속
        conseq = 0 # 현재 연속
        prev_val = sys.float_info.min
        while pq:
            x = heapq.heappop(pq)
            # 연속된 값
            if conseq == 0 or prev_val+1 == x:
                conseq += 1
                max_conseq = max(max_conseq, conseq)
            # 같은 값이 있는 경우
            elif prev_val == x:
                pass
            # 처음 들어온 값이거나 연속이 끊긴 경우
            else:
                conseq = 1
            prev_val = x

        return max_conseq

        


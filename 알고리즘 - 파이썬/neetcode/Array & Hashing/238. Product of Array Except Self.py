class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n)
        # 1. 모두를 곱하고
        # 2. 
        #   - 0이 2개 이상이면 답은 무조건 0, 
        #   - 0이 1개면 답은 0인 것만 전체 곱, 0아닌 것은 0
        #   - 0이 0개면 전체 곱에서 해당 num을 나눈다.
        
        product_val = 1
        zero_cnt = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                product_val *= num
                
        
        result = []
        for num in nums:
            if zero_cnt >= 2:
                return [0 for _ in range(len(nums))]
            elif zero_cnt == 1:
                if num == 0:
                    result.append(product_val)
                else:
                    result.append(0)
            else:
                result.append(product_val // num)
        
        return result

        

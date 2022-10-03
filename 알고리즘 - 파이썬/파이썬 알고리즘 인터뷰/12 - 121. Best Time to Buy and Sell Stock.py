# left, right
import copy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_list = copy.deepcopy(prices) # idx 이전의 최솟값
        max_list = copy.deepcopy(prices) # idx 이후의 최댓값

        for i in range(1, len(prices)):
            min_list[i] = min(min_list[i], min_list[i-1])

        for i in range(len(prices)-2, -1, -1):
            max_list[i] = max(max_list[i], max_list[i+1])

        for i in range(len(prices)):
            result = max(result, max_list[i]-min_list[i])


        return result

# 더 단순하고 직관적인 풀이
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max(prices)
        profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        
        return profit

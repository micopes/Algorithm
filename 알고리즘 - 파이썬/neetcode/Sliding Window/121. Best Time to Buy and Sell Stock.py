class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 이득을 많이 남겨야 한다.
        # 가장 싼 가격에 샀다고 해서 가장 많은 이윤을 남기는 것은 아니다.
        # 사지 않는 것이 더 나을 수 있다.
        # 1. 이중 for 문
        # 2. 누적합처럼, 앞선 가장 작은 수를 구해서 저장 이후에 저장된 값 중 max를 구하면 된다.
        # 3. 슬라이딩 윈도우 및 누적합 개념 이용

        # 3번
        min_prices = copy.deepcopy(prices)
        max_prices = copy.deepcopy(prices)
        n = len(prices)

        for i in range(1, n):
            min_prices[i] = min(min_prices[i], min_prices[i-1])
        
        for i in range(n-2, -1, -1):
            max_prices[i] = max(max_prices[i], max_prices[i+1])

        print(min_prices)
        print(max_prices)

        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, max_prices[i] - min_prices[i])

        return max_profit

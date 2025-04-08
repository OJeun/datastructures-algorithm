class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        min_buy = prices[0]
        max_profit = 0

        for i in range(days):
            min_buy = min(min_buy, prices[i])
            max_profit = max(prices[i] - min_buy, max_profit)

        return max_profit


            
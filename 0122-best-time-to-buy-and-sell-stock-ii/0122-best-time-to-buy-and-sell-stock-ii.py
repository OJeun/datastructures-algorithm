class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for curr in range(len(prices) - 1):
            if prices[curr] < prices[curr + 1]:
                profit += prices[curr + 1] - prices[curr]
            
        return profit

        
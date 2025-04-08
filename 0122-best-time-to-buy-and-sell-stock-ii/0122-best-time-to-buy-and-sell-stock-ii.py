class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr = 0

        while curr < len(prices) - 1:
            if prices[curr] < prices[curr + 1]:
                profit += prices[curr + 1] - prices[curr]
            curr += 1
        
        if profit > 0:
            return profit
        else:
            return 0

        
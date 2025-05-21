class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memoization = [None] * (amount + 1)
        
        def helper(rest_amount):
            minimum = float('inf')

            if rest_amount == 0:
                return 0

            if rest_amount < 0:
                return -1 

            if memoization[rest_amount] is not None:
                return memoization[rest_amount]

            for coin in coins:
                number_of_coin = helper(rest_amount - coin)

                if number_of_coin != -1:
                    minimum = min(minimum, number_of_coin + 1)

            if minimum != float('inf'):
                memoization[rest_amount] = minimum
                return minimum
            else:
                memoization[rest_amount] = -1
                return -1
            
                
        return helper(amount)


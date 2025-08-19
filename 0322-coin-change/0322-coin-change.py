class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        INF = amount + 1

        for i in range(1, amount + 1):
            min_count = INF
            for coin in coins:
                rem = i - coin
                if rem >= 0 and dp[rem] != INF:
                    min_count = min(dp[rem] + 1, min_count)

            dp[i] = min_count
        
        ans = dp[amount]
        return ans if ans is not INF else -1

                
                    













    def coinChange_bottom_up_recursive(self, coins: list[int], amount: int) -> int:
        INF = amount + 1
        dp = [-1] * (amount + 1)

        def dfs(rem):
            if rem < 0:
                return INF

            if rem == 0:
                return 0
            
            if dp[rem] != -1:
                return dp[rem]
            
            min_count = INF
            for coin in coins:
                min_count = min(min_count, dfs(rem - coin) + 1)

            dp[rem] = min_count
            return min_count

        ans = dfs(amount)
        return -1 if ans >= INF else ans
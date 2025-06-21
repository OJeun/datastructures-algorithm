class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1

        def helper(nth_stair):
            if nth_stair <= 1:
                return 1

            if dp[nth_stair] > 0:
                return dp[nth_stair]

            two_steps = helper(nth_stair - 2) 
            one_steps = helper(nth_stair - 1) 

            total = two_steps + one_steps

            dp[nth_stair] = total
            return total

        return helper(n)

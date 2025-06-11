class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0] 
        max_sum = float('-inf')
        n = len(nums)

        for curr in range(n):
            max_sum = max(max_sum, nums[curr] + dp[curr], nums[curr])
            
            max_sum_including_curr = max(nums[curr], nums[curr] + dp[curr])
            dp.append(max_sum_including_curr)

        return max_sum
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float('-inf')
        n = len(nums)

        if n == 1:
            return nums[0]

        for curr in range(1, n):
            max_sum = max(max_sum, nums[curr] + nums[curr - 1], nums[curr], nums[curr - 1])
            max_sum_including_curr = max(nums[curr], nums[curr] + nums[curr - 1])
            nums[curr] = max_sum_including_curr

        return max_sum
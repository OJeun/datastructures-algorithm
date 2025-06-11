class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)

        max_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = num
            else:
                curr_sum += num

            max_sum = max(max_sum, curr_sum)

        return max_sum
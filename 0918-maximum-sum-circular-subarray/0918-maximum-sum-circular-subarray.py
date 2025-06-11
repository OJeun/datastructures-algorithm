class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        max_sum = float('-inf')
        min_sum = float('inf') # minimum sum of subarray
        max_curr_sum = 0
        min_curr_sum = 0
        total_sum = 0

        n = len(nums)

        # track the start index of curr_sum?
        for i in range(n):
            current = nums[i]

            max_curr_sum += current
            min_curr_sum += current
            total_sum += current

            max_sum = max(max_sum, max_curr_sum)
            min_sum = min(min_sum, min_curr_sum)

            if max_curr_sum < 0:
                max_curr_sum = 0

            if min_curr_sum > 0:
                min_curr_sum = 0

        if min_sum != total_sum:
            max_sum = max(max_sum, total_sum - min_sum)
            
        return max_sum
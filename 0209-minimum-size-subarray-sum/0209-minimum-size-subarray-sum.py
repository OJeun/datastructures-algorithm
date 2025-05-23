class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        min_length = float('inf')

        left = 0
        subarray_sum = 0

        for right in range(len(nums)):
            subarray_sum += nums[right]
            if subarray_sum >= target:
               
                while subarray_sum >= target:
                    min_length = min(min_length, right - left + 1)
                    subarray_sum -= nums[left]
                    left += 1


        return 0 if min_length == float('inf') else min_length
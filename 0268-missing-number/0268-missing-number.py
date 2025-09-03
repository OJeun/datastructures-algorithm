class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        for i in range(1, n + 1):
            total += (i - nums[i-1])

        return total
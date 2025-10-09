class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxCount = 0
        curr = 0
        count = 0

        while curr < len(nums):
            if nums[curr] == 1:
                count += 1
                maxCount = max(maxCount, count)

            else:
                count = 0

            curr += 1

        return maxCount
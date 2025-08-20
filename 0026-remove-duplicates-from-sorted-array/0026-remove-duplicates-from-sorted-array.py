class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        next_distinct = 0
        curr = 1

        while curr < len(nums):
            if nums[curr] != nums[curr - 1]:
                next_distinct += 1
                nums[next_distinct] = nums[curr]

            curr += 1

        return next_distinct + 1
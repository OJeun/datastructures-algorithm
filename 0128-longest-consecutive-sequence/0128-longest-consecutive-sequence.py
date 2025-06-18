class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        count = 1
        nums_set = set(nums)

        for num in nums:
            if num - 1 not in nums_set:
                start = num
                end = num
                while end + 1 in nums_set:
                    end += 1
                longest = max(longest, end - start + 1)        
        return longest

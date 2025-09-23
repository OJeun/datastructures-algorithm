class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maximum = 0

        for num in nums_set:
            max_len = 0
            if num - 1 not in nums_set:
                while num in nums_set:
                    max_len += 1
                    num += 1

            maximum = max(max_len, maximum)
                
        return maximum
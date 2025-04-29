class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for num in nums_set:
            count = 1
            if num - 1 not in nums_set:
                while num + 1 in nums_set:
                    count += 1
                    num = num + 1
            
                max_length = max(max_length, count)

        return max_length

            


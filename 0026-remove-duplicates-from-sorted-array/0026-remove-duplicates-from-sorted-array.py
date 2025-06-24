class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicate = set()
        to_be_swapped = 1
        curr = 1
        nums_length = len(nums)

        while curr < nums_length:
            if nums[curr] != nums[curr - 1]:
                nums[to_be_swapped] = nums[curr]
                to_be_swapped += 1
                
            curr += 1

        return to_be_swapped 

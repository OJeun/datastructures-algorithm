class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        curr = 0
        while curr < len(nums) - 1:
            if nums[curr] == nums[curr+1]:
                curr += 1
            else:
                start += 1
                nums[start] = nums[curr+1]
                curr += 1
        
        return start + 1

            
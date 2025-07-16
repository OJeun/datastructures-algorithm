class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        first = nums[0]
        second = nums[first]

        while first != second:
            first = nums[first]
            second = nums[nums[second]]

        slow2 = 0
    
        while slow2 != first:
            slow2 = nums[slow2]
            first = nums[first]

        return first

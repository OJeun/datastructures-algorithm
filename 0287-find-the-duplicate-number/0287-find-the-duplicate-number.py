class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return nums[0]
        
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            fast = nums[nums[fast]]
            slow = nums[slow]

        slow = 0

        while nums[fast] != nums[slow]:
            slow = nums[slow]
            fast = nums[fast]      

        return nums[fast]  
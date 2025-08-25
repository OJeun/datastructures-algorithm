class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = 0
        fast = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break

        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]      

        return slow 
            
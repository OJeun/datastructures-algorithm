class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0

        for curr_index in range(len(nums)):
            if curr_index > max_jump:
                return False
            
            max_jump = max(curr_index + nums[curr_index], max_jump)

        return True
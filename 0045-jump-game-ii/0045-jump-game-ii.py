class Solution:
    def jump(self, nums: List[int]) -> int:
        start_index = 0
        curr_index = 0
        n = len(nums)
        count = 0

        while curr_index < n-1:
            max_jump_index = 0
            max_jump_range = min(n - curr_index, nums[curr_index] + 1)
            for jump in range(1, max_jump_range):
                next_index = curr_index + jump
                if next_index >= n - 1:
                    return count + 1
                if next_index + nums[next_index] > max_jump_index:
                    max_jump_index = next_index + nums[next_index]
                    start_index = next_index
            
            curr_index = start_index
            count += 1
        
        return count
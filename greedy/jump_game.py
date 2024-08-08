# Time Complexity = O(n)
# Space Complexity = O(1)
def can_jump(nums):
    n = len(nums)
    max_index = 0

    for i in range(n):
        if i > max_index:
            return False
        
        jump = i + nums[i]
        max_index = max(max_index, jump)
    
        if max_index >= n-1:
            return True
            
    return False


def can_jumb_recursive(nums):
    n = len(nums)
    goal_index = n - 1

    if n == 0:
        return False

    def helper(goal_index):
        if goal_index <= 0:
            return True
            
        for i in range(1, goal_index+1):
            if (goal_index-i) + nums[goal_index-i] >= goal_index:
                return helper(goal_index - i)
            
        return False
        
    return helper(goal_index)


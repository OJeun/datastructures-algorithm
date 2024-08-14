def can_jump_recursive(nums):
    n = len(nums)
    goal_index = n - 1

    if n == 0:
        return False
        
    def helper(position):
        if position == goal_index:
            return True
        next_furthest_jump_position = min(position+nums[position], goal_index)
        for index in range(position + 1, next_furthest_jump_position + 1):
            if helper(index):
                return True
        return False
        
    return helper(0)

def can_jump_memoization(nums):
    n = len(nums)
    goal_index = n - 1
    dp = [-1] * n

    if n == 0:
        return False
        
    def helper(position):
        if dp[position] != -1:
            return dp[position]
        if position == goal_index:
            return True
        next_furthest_jump_position = min(position+nums[position], goal_index)
        for index in range(position + 1, next_furthest_jump_position + 1):
            if helper(index):
                dp[index] = True
        dp[position] = False
        
    return helper(0)

def can_jump_tabulation(nums):
    n = len(nums)
    if n == 0:
        return False
    
    dp = [False] * n
    dp[0] = True

    for i in range(n):
        if dp[i]:
            max_jump_position = min(n-1, i + nums[i])
            for j in range(i+1, max_jump_position+1):
                dp[j] = True
    
    return dp[n-1]
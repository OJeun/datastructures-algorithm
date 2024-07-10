def can_partition(nums):
    total = sum(nums)
    length_of_nums = len(nums)
    
    if total % 2 != 0:
        return False
        
    target = total // 2
    
    def helper(index, curr_sum):
        if curr_sum == target:
            return True
            
        if index > length_of_nums - 1 or curr_sum > target:
            return False
    
        # Include
        include = helper(index + 1, curr_sum + nums[index])
        
        # Exclude
        exclude = helper(index + 1, curr_sum)
        
        return include or exclude
    
    return helper(0, 0)

def can_partition_memoization(nums):
    total = sum(nums)
    length_of_nums = len(nums)
    
    if total % 2 != 0:
        return False
        
    target = total // 2
    dp = [[None]*(2 * target + 1) for _ in range(length_of_nums)]
    
    def helper(index, curr_sum):
        if curr_sum == target:
            return True
            
        if index > length_of_nums - 1 or curr_sum > target:
            return False
            
        if dp[index][target+curr_sum] != None:
            return dp[index][target+curr_sum]
    
        # Include
        include = helper(index + 1, curr_sum + nums[index])
        
        # Exclude
        exclude = helper(index + 1, curr_sum)
        
        dp[index][target + curr_sum] = include or exclude
        return dp[index][target + curr_sum]
    
    return helper(0, 0)
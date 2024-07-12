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
    dp = [[None]*(target + 1) for _ in range(length_of_nums)]
    
    def helper(index, curr_sum):
        if curr_sum == target:
            return True
            
        if index > length_of_nums - 1 or curr_sum > target:
            return False
            
        if dp[index][target+curr_sum] != None:
            return dp[index][curr_sum]
    
        # Include
        include = helper(index + 1, curr_sum + nums[index])
        
        # Exclude
        exclude = helper(index + 1, curr_sum)
        
        dp[index][curr_sum] = include or exclude
        return dp[index][curr_sum]
    
    return helper(0, 0)

# nums = [1, 5, 11, 5]
def can_partition_with_tabulation_sol(nums):
    n = len(nums)
    sum = sum(nums)

    if sum % 2 != 0: return False
    target =sum//2
    prev = [False] * (target + 1) 
    curr = [False] * (target + 1)
    prev[0] = True
    curr[0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            #pick
            if nums[i-1] <= j:
                # by adding nums[i-1] on prev[j-nums], can achieve curr[j]
                curr[j] = prev[j-nums[i-1]]
            else:
                curr[j] = False    
            #dontpick
            curr[j] = curr[j] or prev[j]
            
        prev = curr[:]  
    return curr[target] 

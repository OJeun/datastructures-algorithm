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


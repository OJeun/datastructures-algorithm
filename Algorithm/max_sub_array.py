def max_subarray(nums):
    if not nums:
        return 0
        
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, num+current_sum)
        max_sum = max(max_sum, current_sum)
        
    return max_sum
    

def remove_element(nums, val):    
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    
    return len(nums)

nums = [1,2,3,4,3,5]
remove_element(nums, 3)
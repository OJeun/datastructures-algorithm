def maxProduct(nums):
    curr_min = 1
    curr_max = 1
    max_product = max(nums)
    
    for num in nums:
        if num == 0:
            curr_min = 1
            curr_max = 1
        else:
            a = curr_min * num
            b = curr_max * num
            
            curr_min = min(a, b, num)
            curr_max = max(a, b, num)
            
            if curr_max > max_product:
                max_product = curr_max

    return max_product
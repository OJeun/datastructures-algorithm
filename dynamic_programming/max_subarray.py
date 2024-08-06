def max_sub_array_1D_tabluation(nums):
    length_nums = len(nums)
    
    if length_nums == 0:
        return 0
        
    dp = [0] * length_nums
    dp[0] = nums[0]
    max_sum = nums[0]

    for index in range(1, length_nums):
        maximum = max(nums[index], dp[index-1] + nums[index])
        dp[index] = maximum
        max_sum = max(max_sum, maximum)
    return max_sum
        
def max_sub_array(nums):
    n = len(nums)
    if n == 0:
        return 0
    max_sum = nums[0]
    prev_sum = 0

    for num in nums:
        prev_sum = max(num, prev_sum+num)
        max_sum = max(prev_sum, max_sum)

    return max_sum


nums = [1,2,-10]
print(max_sub_array(nums))
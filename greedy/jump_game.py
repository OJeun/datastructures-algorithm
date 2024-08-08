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
        

print(can_jump([1,1,1,1,1,1]))

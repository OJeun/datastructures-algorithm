# Time complexity = O(2^n)
# Space compleixty = O(n)

def length_of_LIS(nums):
    #write code here
    def helper(curr, prev):
        if curr > len(nums) - 1:
            return 0
        
        exclude = helper(curr + 1, prev)

        include = 0
        if prev == -1 or nums[curr] > nums[prev]:
            include = 1 + helper(curr + 1, curr)
    
        return max(exclude, include)
    
    return helper(0, -1)

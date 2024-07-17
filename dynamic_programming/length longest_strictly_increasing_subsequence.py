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

# Time Complexity = O(n^2)
# Space Complexity = O(n^2)
def length_of_LIS_memoization(nums):
    length_num = len(nums)

    dp = [[-1] * length_num for _ in range(length_num)]

    def helper(curr, prev):
        if curr > length_num - 1:
            return 0
        
        if dp[prev+1][curr] != -1:
            return dp[prev+1][curr] 

        exclude = helper(curr + 1, prev)

        include = 0
        if prev == -1 or nums[curr] > nums[prev]:
            include = 1 + helper(curr + 1, curr)
    
        dp[prev+1][curr] = max(exclude, include)
        return dp[prev+1][curr] 
    
    return helper(0, -1)
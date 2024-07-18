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

# Time Complexity = O(n^2)
# Space Complexity = O(n^2)
def length_of_LIS_tabulation(nums):
    length_num = len(nums)

    dp = [[-1] * (length_num+1)for _ in range(length_num+1)]

    for i in range(length_num+1):
        dp[length_num][i] = 0

    for j in range(length_num+1):
        dp[j][length_num] = 0

    
    for curr in range(length_num-1, -1, -1):
        for prev in range(curr, -1, -1):
            include = 0
            if prev == 0 or nums[curr] > nums[prev-1]:
                include = 1 + dp[curr+1][curr+1]
            
            exclude = dp[curr+1][prev]

            dp[curr][prev] = max(include, exclude)

    return dp[0][0]

def length_of_LIS_optimized_tabulation(nums):
    length_num = len(nums)

    curr = [0] * (length_num + 1)
    next = [0] * (length_num + 1)

    
    for row in range(length_num-1, -1, -1):
        for col in range(row, -1, -1):
            include = 0
            if col == 0 or nums[row] > nums[col-1]:
                include = 1 + next[row+1]
            
            exclude = next[col]

            curr[col] = max(include, exclude)
        
        next = curr[:]

    return curr[0]
    
# Time Complexity = O(n^2)
# Space Complexity = O(n)
def length_of_LIS_1D_tabulation(nums):
    length_num = len(nums)
    dp = [1] * (length_num + 1)
    dp[0] = 1
    max = 1

    for i in range(1, length_num):
        for j in range(i):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
            
            if dp[i] > max:
                max = dp[i]
            
    return max
    
    
print(length_of_LIS_1D_tabulation([2,8,3,7]))
# Time complexity = O(3^(n+m))
# Space Complexity = O(n+m)
def edit_distance(text1, text2):
    len_1 = len(text1)
    len_2 = len(text2)

    def helper(index1, index2):        
        # Base Case
        if index2 > len_2 - 1:
            return len_1 - index1
        
        if index1 > len_1 - 1:
            return len_2 - index2
        
        # Recursive
        # Equal
        if text1[index1] == text2[index2]:
            return helper(index1+1, index2+1)
        
        # Not Equal
        insert = 1 + helper(index1, index2+1)
        delete = 1 + helper(index1, index2)
        replace = 1 + helper(index1+1, index2+1)

        return min(insert, delete, replace)
    
    return helper(0,0)

# Space Complexity = O(n * m) + O(n + m) = O(n * m)
# Time Complexity = O(n * m)
def edit_distance_memoization(text1, text2):
    len_1 = len(text1)
    len_2 = len(text2)
    dp = [[-1] * len_1 for _  in range(len_2)]

    def helper(index1, index2):        
        # Base Case
        if index2 > len_2 - 1:
            return len_1 - index1
        
        if index1 > len_1 - 1:
            return len_2 - index2
        
        if dp[index1][index2] != -1:
            return dp[index1][index2]
        
        # Recursive
        # Equal
        if text1[index1] == text2[index2]:
            dp[index1][index2] = helper(index1+1, index2+1)
        
        # Not Equal
        insert = 1 + helper(index1, index2+1)
        delete = 1 + helper(index1+1, index2)
        replace = 1 + helper(index1+1, index2+1)

        dp[index1][index2] = min(insert, delete, replace)
        return dp[index1][index2]
    
    return helper(0,0)

# Space Complexity = O(n * m)
# Time Complexity = O(n * m)
def edit_distance_tabulation(text1, text2):
    len_1 = len(text1)
    len_2 = len(text2)
    dp = [[-1] * (len_1 + 1) for _  in range(len_2+1)]
    
    for j in range(len_2+1):
        dp[0][j] = j
    
    for j in range(len_1+1):
        dp[j][0] = j

    for row in range(1, len_2 + 1):
        for col in range(1, len_1 + 1):
            if text2[row] == text1[col]:
                dp[row][col] = dp[row-1][col-1]
            else:
                top = 1 + dp[row-1][col]
                left = 1 + dp[row][col-1]
                diagonal = 1 + dp[row-1][col-1]
                dp[row][col] = min(top, left, diagonal)

    return dp[len_2][len_1]

# Time complexity = O(m*n)
# Space Complexity = O(m) or O(n)
def edit_distance_optimized_tabulation(text1, text2):
    len_1 = len(text1)
    len_2 = len(text2)
    prev = [0] * len_1
    curr = [0] * len_1

    for j in range(len_2+1):
        prev[j] = j

    for row in range(1, len_2+1):
        curr[0] = row
        for col in range(1, len_1+1):
            if text1[col-1] == text2[row-1]:
                curr[col] = prev[col-1]
            else:
                replace = 1 + prev[col-1]
                delete = 1 + prev[col]
                insert = 1 + curr[col-1]
                curr[col] = min(replace, delete, insert)
        prev = curr[:]
    return curr[len_1]
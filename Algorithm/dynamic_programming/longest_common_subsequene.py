# Time complexity = O(2^(n + m))
# Space Complexity = O(n + m)
def longest_common_subsequence(text1, text2):
    length_t1 = len(text1)
    length_t2 = len(text2)
    
    
    def helper(index1, index2):
        # BaseCase
        if index1 > length_t1 - 1 or index2 > length_t2 - 1:
            return 0
        
        # RecursiveClass
        # Equal
        if text1[index1] == text2[index2]:
            res = 1 + helper(index1 + 1, index2 + 1)
            return res

        # Not Equal
        include_index_in_text1 = helper(index1, index2 + 1) 
        exclude_index_in_text1 = helper(index1 +1 , index2)
        
        return max(include_index_in_text1, exclude_index_in_text1)
    return helper(0, 0)

# Time complexity = O(n+m)
# Space Complexity = O(n + m) + O(n*m)
def longest_common_subsequence_memoization(text1, text2):
    length_t1 = len(text1)
    length_t2 = len(text2)
    dp = [[None] * length_t1 for _ in range(length_t2)]
    
    def helper(index1, index2):
        # BaseCase
        if index1 > length_t1 - 1 or index2 > length_t2 - 1:
            return 0
        
        if dp[index2][index1] != None:
            return dp[index2][index1]
        
        # RecursiveClass
        # Equal
        if text1[index1] == text2[index2]:
            res = 1 + helper(index1 + 1, index2 + 1)
            dp[index2][index1] = res
            return dp[index2][index1]

        # Not Equal
        include_index_in_text1 = helper(index1, index2 + 1) 
        exclude_index_in_text1 = helper(index1 +1, index2)
        
        dp[index2][index1] = max(include_index_in_text1, exclude_index_in_text1)
        return dp[index2][index1]
        
    return helper(0, 0)

# Time Complexity = O(n * m)
# Space Complexity = O(n * m)
def longest_common_subsequence_tabulation(text1, text2):
    length_t1 = len(text1) # pbcdq
    length_t2 = len(text2) # pcq
 
    dp = [[0] * (length_t1 + 1) for _ in range(length_t2+1)]
    print(dp)

    for index1 in range(1, length_t1 + 1):
        for index2 in range(1, length_t2 + 1):
            if text1[index1 - 1] == text2[index2 - 1]:
                dp[index2][index1] = dp[index2 - 1][index1 - 1] + 1
            else: 
                left = dp[index2 - 1][index1]
                top = dp[index2][index1 - 1]
                dp[index2][index1] = max(left, top)
    return dp[length_t2][length_t1]

# Time Complexity = O(n * m)
# Space Commplexity = O(min(m, n))
def longest_common_subsequence_optimized_tabulation(text1, text2):
    length_t1 = len(text1) # pbcdq
    length_t2 = len(text2) # pcq
 
    # dp = [[0] * (length_t1 + 1) for _ in range(length_t2+1)]
    prev = [0] * (length_t1 + 1)
    curr = [0] * (length_t1 + 1)

    for index2 in range(1, length_t2 + 1):
        for index1 in range(1, length_t1 + 1):
            if text1[index1 - 1] == text2[index2 - 1]:
                curr[index1] = prev[index1 - 1] + 1
            else: 
                left = curr[index1 - 1]
                top = prev[index1]
                curr[index1] = max(left, top)
        prev = curr[:]

    return curr[length_t1]

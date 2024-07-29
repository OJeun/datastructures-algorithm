# Time complexity = O(n * 2^n)
def min_cut(s):
    length_s = len(s)
    def is_palindrome(i, j):
        if i == j:
            return True
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def partitions(start, end):
        # Base Case
        if start == end or is_palindrome(start, end):
            return 0
        
        # Recursion
        minimum = end - start
        for j in range(start, end):
            if is_palindrome(start, j):
                minimum = min(minimum, 1+partitions(j+1, end))
        return minimum
    return partitions(0, length_s -1)

# Space Complexity = O(n^2)
# Time Complexity = O(n^2)
def min_cut_memoization(s):
    length_s = len(s)

    # Time Complexity = O(n^2)
    # Space Complexity = O(n^2)
    def is_palindrome(s):
        dp = [[-1] * length_s for _ in range(length_s)]
        
        for length in range(1, length_s + 1):
            for row in range(length_s - length + 1):
                col = row + length - 1
                    
                if row == col:
                    dp[row][col] = True
                    
                elif s[row] == s[col] and (col == row + 1 or dp[row+1][col-1]):
                    dp[row][col] = True
                    
                else:
                    dp[row][col] = False
        return dp
    
    palindrome_dp = is_palindrome(s)
    dp = [[-1] * length_s for _ in range(length_s)]

    def partitions(start, end):
        # Base Case
        if start == end or palindrome_dp[start][end]:
            return 0

        if dp[start][end] != -1:
            return dp[start][end]
        
        # Recursion
        minimum = end - start
        for j in range(start, end):
            if palindrome_dp[start][j]:
                minimum = min(minimum, 1+partitions(j+1, end))
        dp[start][end] = minimum
        return dp[start][end]
    
    return partitions(0, length_s -1)    

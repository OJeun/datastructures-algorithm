def is_palindrome(s):
    s_length = len(s)
    dp = [[-1] * s_length for _ in range(s_length)]
    
    for length in range(1, s_length + 1):
        for row in range(s_length - length + 1):
            col = row + length - 1
                
            if row == col:
                dp[row][col] = True
                
            elif s[row] == s[col] and (col == row + 1 or dp[row+1][col-1]):
                dp[row][col] = True
                
            else:
                dp[row][col] = False
    return dp
print(is_palindrome("ppq"))

# Space Complexity = O(n^2)
# Time Complexity = O(n^n)
def partition(s):
    s_length = len(s)
    output = []
    dp = is_palindrome(s)
    
    def helper(index, curr):
        if index > s_length - 1:
            output.append(curr[:])
            return
        
        for j in range(index, s_length):
            if dp[index][j] == True:
                curr.append(s[index:j+1])
                helper(j + 1,curr)
                curr.pop()
    helper(0, [])
    return output

print(partition("ppq"))
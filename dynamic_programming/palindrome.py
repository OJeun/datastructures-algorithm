# Time complexity = O(n^2)
# Space Complexity = O(n^2)
def countSubstrings(s):
    n = len(s) # n = 6
    dp = [[-1] * n for _ in range(n)]
    count = 0
    
    for i in range(n):
        dp[i][i] = True # lenght = 1 -> true 
        count += 1
        
    for row in range(n - 2, -1, -1): # 4 to 0
        for col in range(row + 1, n):  
            if s[row] == s[col] and (col == row + 1 or dp[row+1][col-1]):
                dp[row][col] = True
                count += 1
            else:
                dp[row][col] = False
    return count

print(countSubstrings("pqprps"))

def countSubstrings(s):
    n = len(s) # n = 6
    dp = [[-1] * n for _ in range(n)]
    count = 0
    
    for i in range(n):
        dp[i][i] = True # lenght = 1 -> true 
        count += 1

    for i in range(n-1): # 0 to 4
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            count += 1
        else:
            dp[i][i+1] = False

    for length in range(3, n+1): # 3 to 6
        for start in range(n-length+1):
            end = start + length - 1
            if s[start] == s[end] and dp[start+1][end-1]:
                dp[start][end] = True
                count += 1
            else:
                dp[start][end] = False
    return count

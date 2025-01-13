def countSubstrings_recursive_with_memoization(s):
    n = len(s)
    dp = [[-1]*n for _ in range(n)]

    def helper(i,j):
        if i==j:
            dp[i][j]=True
            return dp[i][j]

        if dp[i][j]!= -1:
            return dp[i][j]    
        helper(i+1,j)
        helper(i,j-1)
        if s[i]==s[j] and (j==i+1 or helper(i+1,j-1)):
            dp[i][j] = True
        else:
            dp[i][j] = False   
        return dp[i][j]     
    helper(0,n-1)

    #count the number of times we have True in dp
    res = 0
    for l in range(1,n+1):
        for i in range(n-l+1):
            j = i+l - 1   
            if dp[i][j] ==True:
                res+=1
    return res            

# Time complexity = O(n^2)
# Space Complexity = O(n^2)
def countSubstrings_tabulation_2(s):
    res = 0
    n = len(s)

    dp = [[0]*n for _ in range(n)]

    for l in range(1,n+1):
        for i in range(n-l+1):
            j = i+l - 1
            if i==j: 
                dp[i][j] = True
                res+=1
            elif s[i]==s[j] and (j==i+1 or dp[i+1][j-1]):
                dp[i][j] = True
                res +=1
            else:
                dp[i][j] = False
    return res     
        

def countSubstrings_tabulation_2(s):
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

def longest_palindrome_subseq(s):
    res = 0
    n = len(s)

    dp = [[0] *n for _ in range(n)]

    for l in range(1,n+1):
        for i in range(n-l+1):
            j = i+l - 1
            if i==j: 
                dp[i][j] = 1
                
            elif s[i]==s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]

            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                
    return dp[0][n-1]  
def countSubstrings(s):
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

s = "v"
print(countSubstrings(s))
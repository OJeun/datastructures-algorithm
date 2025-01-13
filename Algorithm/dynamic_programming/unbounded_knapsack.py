def unbounded_knap_sack(W, wt, val, n):
    # val = [2, 3, 9]
    # wt = [8, 2, 5]
    def helper(index, remain_weight):
        # Base Case
        if index > n - 1 or remain_weight == 0:
            return 0
        
        # Recusrive Case
        exclude = helper(index + 1, remain_weight)
        include = 0
        if wt[index] <= remain_weight:
            include = val[index] + helper(index, remain_weight-wt[index])

        return max(exclude, include)

    return helper(0, W)


# Time Complexity = O(n * W)
# Space Complexity = O(n * W)
def unbounded_knap_sack_tabulation(W, wt, val, N):
    # code here
    dp = [[-1]*(W+1) for _ in range(N+1)]
    
    for j in range(W+1):
        dp[0][j] = 0
    
    for i in range(N+1):
        dp[i][0] = 0
    
    for i in range(1,N+1):
        for j in range(1,W+1):
            exclude = dp[i-1][j]
            include = 0
            if wt[i-1] <=j:
                include = val[i-1] + dp[i][j -wt[i-1]]
            dp[i][j] = max(exclude,include)
    return dp[N][W]
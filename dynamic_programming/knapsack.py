# The hint of dp problem = choices(include, exclude) => recursion, optimal solution(maximum)
def knap_sack_1(W, wt, val, n):
    
    def helper(sum_weight, sum_value, index):        
        if sum_weight == W:
            return sum_value
            
        if sum_weight > W:
            sum_value -= val[index - 1]
            return sum_value
        
        if index > n - 1 and sum_weight > W:
            return 0
        
        if index > n - 1:
            return sum_value

        # Include
        new_sum_weight = sum_weight + wt[index]
        new_sum_value = sum_value + val[index]
        include = helper(new_sum_weight, new_sum_value, index+1)
        
        # Exclude
        exclude = helper(sum_weight, sum_value, index + 1)

        return max(include, exclude)
    return helper(0, 0, 0)

# Time complexity = O(2^n)
# Space complexity = O(n)

def knap_sack_2(W, wt, val, n):
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
            include = val[index] + helper(index + 1, remain_weight-wt[index])
        return max(exclude, include)

    return helper(0, W)


# Time Complexity = O(n * W)
# Space Complexity = O(n * W)
def knap_sack_memoization(W, wt, val, n):
    memoization_table = [[-1] * (W + 1) for _ in range(n)]
    def helper(index, remain_weight):
        # Base Case
        if memoization_table[index][remain_weight] != -1:
            return memoization_table[index][remain_weight]

        if index > n - 1 or remain_weight == 0:
            return 0
        
        # Recusrive Case
        exclude = helper(index + 1, remain_weight)
        include = 0
        if wt[index] <= remain_weight:
            include = val[index] + helper(index + 1, remain_weight-wt[index])
        memoization_table[index][remain_weight] = max(exclude, include)
        return memoization_table[index][remain_weight]

    return helper(0, W)

# Space Complexity = O(n * W)
# Time Complexity = O(n * W)
def knap_sack_tabulation(W, wt, val, n):
    memoization_table = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            exclude = memoization_table[i-1][j]
            include = 0
            if wt[j-1] <= j:
                include = val[i -1] + memoization_table[i-1][j - wt[i-1]]
            memoization_table[i][j] = max(include, exclude)

    return memoization_table[n][W]

# Space Complexity = O(W)
# Time Complexity = O(m * W)
def knap_sack_optimised_tabulation(W, wt, val, n):
    prev = [0] * (W + 1)
    curr = [0] * (W + 1)

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            exclude = prev[j]
            include = 0
            if wt[j-1] <= j:
                include = val[i -1] + prev[j - wt[i-1]]
            curr[j] = max(include, exclude)
        prev = curr[:]

    return curr[W]




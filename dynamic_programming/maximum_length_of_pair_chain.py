def find_longest_chain_recursive(pairs):
    length = len(pairs)
    sorted_pairs = sorted(pairs, key=lambda x: x[0])

    def helper(curr, prev):
        if curr > length -1:
            return 0
            
        exclude = helper(curr + 1, prev)
        
        include = 0
        if prev == -1 or sorted_pairs[curr][0] > sorted_pairs[prev][1]:
            include = 1 + helper(curr + 1, curr)

        return max(exclude, include)
        
    return helper(0, -1)

def find_longest_chain_memoization(pairs):
    length = len(pairs)
    sorted_pairs = sorted(pairs, key=lambda x: x[0])

    dp = [[-1] * length for _ in range(length)]

    def helper(curr, prev):
        if curr > length -1:
            return 0
        
        if dp[curr][prev+1] != -1:
            return dp[curr][prev+1]
            
        exclude = helper(curr + 1, prev)
        
        include = 0
        if prev == -1 or sorted_pairs[curr][0] > sorted_pairs[prev][1]:
            include = 1 + helper(curr + 1, curr)

        dp[curr][prev+1] = max(exclude, include)
        return dp[curr][prev+1]
        
    return helper(0, -1)

def find_longest_chain_tabulation(pairs):
    length = len(pairs)
    sorted_pairs = sorted(pairs, key=lambda x: x[0]) # time = O(nlogn)

    dp = [[-1] * (length+1) for _ in range(length+1)]

    for i in range(length+1):
        dp[3][i] = 0
        dp[i][3] = 0

    for row in range(length-1, -1, -1):
        for col in range(row, -1, -1):
            exclude = dp[row+1][col]
            include = 0
            if col == 0 or sorted_pairs[row-1][1] < sorted_pairs[row][0]:
                include = 1 + dp[row+1][row]
            dp[row][col] = max(include, exclude)

    return dp[0][0]

def find_longest_chain_1D_tabulation(pairs):
    length = len(pairs)
    sorted_pairs = sorted(pairs, key=lambda x: x[0]) 
    longest = 1
    dp = [1] * length

    for i in range(1, length):
        for j in range(i):
            if sorted_pairs[i][0] > sorted_pairs[j][1] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
        if dp[i] >  longest: longest = dp[i]
    
    return longest


pairs = [[4, 5],[2, 9],[1, 2]]
print(find_longest_chain_1D_tabulation(pairs))


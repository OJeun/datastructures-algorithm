# Space Complexity = O(n)
# TIme Complexity = O(n * 2^n) 2^n: number of partitions 
def matrix_chain_multiplication(N, arr):
    
    def partitions(start, end):
        if start == end:
            return 0
    
        min_cost = float('inf')
        for partition in range(start, end):
            curr_cost = partitions(start, partition) + partitions(partition+1, end) + (arr[start-1] * arr[partition] * arr[end])
            min_cost = min(min_cost, curr_cost)

        return min_cost

    return partitions(1, N-1)

# Time Complexity = O(n^3) n^2: partition combination * n: for loop
# Space Complexity = O(n^2)
def matrix_chain_multiplication_memoization(N, arr):
    dp = [[-1] * (N-1) for _ in range(N-1)]
    
    def partitions(start, end):
        if start == end:
            dp[start-1][end-1] = 0
            return dp[start-1][end-1]
    
        min_cost = float('inf')
        for partition in range(start, end):
            curr_cost = partitions(start, partition) + partitions(partition+1, end) + (arr[start-1] * arr[partition] * arr[end])
            min_cost = min(min_cost, curr_cost)

        dp[start-1][end-1] = min_cost
        return dp[start-1][end-1] 

    return partitions(1, N-1)

def matrix_chain_multiplication_tabulation(N, arr):
    dp = [[0] * (N) for _ in range(N)]

    for length in range(2, N+1):
        for row in range(N -length +1):
            col = length + row - 1
            min_cost = float('inf')
            for partition in range(row+1, col):
                min_cost = min(min_cost, dp[row+1][partition] + dp[partition+1][col] + arr[row+1] * arr[partition] * arr[col])
            dp[row][col] = min_cost
    return dp[0][N]


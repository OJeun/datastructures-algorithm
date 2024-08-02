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
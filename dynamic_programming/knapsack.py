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
    
print(knap_sack_2(8, [8, 2, 5], [2,3,9], 3))
    
    
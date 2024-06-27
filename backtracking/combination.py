# Time Complexity = Number of Nodes * work done at each node
#                 = k * nCk * O(1)   # k = the number of recursive calls for each result node
# Space Complexity = O(k) # Recursive call stack

def combine(nums,k):
    output = []
    def helper(index, subset):
        if len(subset) == k:
            output.append(subset.copy())
            return
            
        for j in range(index, nums + 1):
            subset.append(j)
            helper(index+1, subset)
            subset.pop()

    helper(1, [])
    return output
    
def combine_with_optimization(nums,k):
    output = []
    def helper(index, subset):
        if len(subset) == k:
            output.append(subset.copy())
            return
        need = k - len(subset)  
        for j in range(index, nums - (need - 1) + 1):
            subset.append(j)
            helper(index+1, subset)
            subset.pop()

    helper(1, [])
    return output
        
    

# N = # of candidates
# T = target
# M = minimum value among candidates

# 1) Max depth of the recursion tree = T / M
# 2) Total number of the nodes = N^(T/M)

# Time Complexity = O(N^(T/M)) * O(1)
# Space Complexity = O(T/M) # recursion stack


def combination_sum(candidates, target):
    output = []
    def helper(i, curr, curr_sum):
        if curr_sum == target:
            output.append(curr.copy())
            return
        if curr_sum > target:
            return
        
        for j in range(i, len(candidates)):
            curr.append(candidates[j])
            helper(j, curr, curr_sum + candidates[j])
            curr.pop()
    helper(0, [], 0)
    return output
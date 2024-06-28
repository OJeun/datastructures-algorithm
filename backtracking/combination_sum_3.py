# Space Complexity = O(k)

def combination_sum_3(k, n):
    # n = target
    # k = the number of value
    nums = [1,2,3,4,5,6,7,8,9] 
    res = []
    def backtrack(index, curr_sum, curr):
        if curr_sum == n and len(curr) == k:
            res.append(curr.copy())
        if curr_sum > n:
            return
        if len(curr) == k:
            return
        for j in range(index, len(nums)):
            element = nums[j]
            curr.append(element)
            backtrack(j+1, curr_sum+element, curr)
            curr.pop()
    backtrack(0,0,[])
    return res

print(combination_sum_3(3,7))
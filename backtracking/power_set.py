# Time Complexity = O(n * 2^n)
# Space Complexity = O(n)
def power_set(nums):
    output = []
    def helper(index, nums, subset):
        if index == len(nums):
            output.append(subset.copy())
            return
        
        # Exclude part
        helper(index + 1, nums, subset)

        # Include part
        subset.append(nums[index])
        helper(index + 1, nums, subset)
        subset.pop()
    helper(0, nums, [])
    return output
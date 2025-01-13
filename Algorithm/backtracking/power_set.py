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


# psuedo code
# if i == length, push
#     to result
# # exclude
# helper(i+1, nums, subset)

# # include
# push nums[i] to subset
# helper(i+1, nums, subset)
# pop last element from subset


# Time complexity = O(2^n * n)
# Space complexity = O(n)
def power_set_with_duplication(nums):
    output = []
    def helper(index, subset):
        if index == len(nums):
            output.append(subset.copy())
            return
        
        # Include part
        subset.append(nums[index])
        helper(index + 1, subset)
        subset.pop()

        # Exclusive part
        while(index < len(nums) -1 and nums[index] == nums[index+1]):
            index += 1
        helper(index + 1, subset)
    
    helper(0, [])
    return output

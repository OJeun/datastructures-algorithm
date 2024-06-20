def permutation(nums):
    result = []
    if len(nums) == 1:
        return [nums]
    perms = permutation(nums[:-1])
    inserted_element = nums[-1]
    for perm in perms:
        for i in range(len(perm) + 1):
            copied_perm = perm[:]
            copied_perm.insert(i, inserted_element)
            result.append(copied_perm)
    return result
    
# Time complexity = O(n * n!)
# Space complexity = O(n)
def permute(nums):
    result = []

    def helper(index):
        nums_length = len(nums)
        if index == nums_length - 1:
            result.append(nums[:]) # making a copy of an array is O(n)
            return
        for j in range(index, nums_length):
            nums[j], nums[index] = nums[index], nums[j]
            helper(index + 1)
            nums[j], nums[index] = nums[index], nums[j]
    helper(0)
    return result
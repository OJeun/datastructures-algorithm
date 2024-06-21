# Time complexity = O(n * n!)
# Space complexity = O(n)
def permutation_basic_recursive(nums):
    result = []
    if len(nums) == 1:
        return [nums]
    perms = permutation_basic_recursive(nums[:-1])
    inserted_element = nums[-1]
    for perm in perms:
        for i in range(len(perm) + 1):
            copied_perm = perm[:] # O(n)
            copied_perm.insert(i, inserted_element)
            result.append(copied_perm)
    return result
    
# Time complexity = O(n * n!)
# Space complexity = O(n)
def permute_without_duplication(nums):
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

# Time complexity = O(n * n!)
# Space complexity = O(n)
def permute_with_duplication(nums):
    #write code here
    result = []
    def helper(index):
        hash_table = {}
        length_of_nums = len(nums)
        if index == length_of_nums-1:
            result.append(nums[:])
            return
        for j in range(index, length_of_nums):
            if nums[j] not in hash_table: # O(1)
                hash_table[nums[j]] = True # O(1)
                nums[index], nums[j] = nums[j], nums[index]
                helper(index + 1)
                nums[index], nums[j] = nums[j], nums[index]
            continue
    helper(0)
    return result

print(permute_with_duplication([2,2,3]))
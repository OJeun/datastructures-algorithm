class Solution:
    def subsets(self, nums: list[int]):
        subsets = []
        len_nums = len(nums)

        def helper(index, subset_list):
            if index > len_nums - 1:
                subsets.append(subset_list)
                return

            element = nums[index]

            # Include
            inclusive_subset = subset_list[:]  
            inclusive_subset.append(element)  
            helper(index + 1, inclusive_subset)

            # Exclude
            exclusive_subset = subset_list[:]  
            helper(index + 1, exclusive_subset)

        helper(0, [])
        return subsets
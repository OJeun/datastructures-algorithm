class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {val:index for index, val in enumerate(nums)}

        for i in range(len(nums)):
            substraction = target - nums[i]
            index = nums_dict.get(substraction)
            if index and index > i:
                return [nums_dict[substraction], i]
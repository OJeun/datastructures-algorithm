class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look_up = dict()

        # Iterate nums and calculate the complement of each number and check it is in dictionary and it is not the same as the used number
        for index, num in enumerate(nums):
            complement = target - num

            if complement in look_up:
                return [index, look_up[complement]]
            
            look_up[num] = index

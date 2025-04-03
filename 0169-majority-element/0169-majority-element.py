class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        majority = 0
        majority_element = 0

        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1

        for element, count in my_dict.items():
            if count > majority:
                majority = count
                majority_element = element

        return majority_element
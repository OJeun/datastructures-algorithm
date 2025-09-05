class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        frequency = dict()
        thirdMaxReturn = float("-inf")

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        distincted_list = list(frequency.keys())

        if len(distincted_list) < 3:
            return max(distincted_list)

        for _ in range(3):
            thirdMaxReturn = max(distincted_list)
            distincted_list.remove(thirdMaxReturn)

        return thirdMaxReturn

            


        
        
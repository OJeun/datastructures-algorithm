class Solution:
    def rob(self, nums: list[int]) -> int:
        memoization = [-1] * len(nums)

        def helper(n) -> int: 
            index = n - 1

            if n == 0:
                return 0

            if n == 1:
                memoization[index] = nums[index]
                return nums[index]
            
                
            if memoization[index] != -1:
                return memoization[index]
            else:
                max_rob_to_nth_house = max(helper(n - 1), nums[index] + helper(n - 2))
                memoization[index] = max_rob_to_nth_house
                return max_rob_to_nth_house

        return helper(len(nums))
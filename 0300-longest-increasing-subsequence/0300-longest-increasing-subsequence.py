class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        nums_length = len(nums)
        max_return = 1
        dp = {}

        def helper(start):
            if start == nums_length - 1:
                return 1
            
            if dp.get(start) is not None:
                return dp.get(start)

            result = 1

            for index in range(start + 1, nums_length):
                if nums[index] > nums[start]:
                    result = max(result, helper(index) + 1)

            dp[start] = result
            return result

        for i in range(nums_length):
            max_return = max(max_return, helper(i))

        return max_return

                
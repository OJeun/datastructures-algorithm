class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        # define a helper func(index) => maximum sum up to ith house
        def helper(index) -> int:
            # will check maximum at index -1 and index -2 return maximum money
            if index < 0:
                return 0

            if dp[index] != -1:
                return dp[index]

            # past_one = helper(index - 1)
            exclude = helper(index - 1)

            # past_two = helper(index - 2)
            include = nums[index] + helper(index - 2)

            # maximum_up_to_index = max(past_one, past_two + nums[index])
            max_up_to_index = max(exclude, include)

            dp[index] = max_up_to_index

            return max_up_to_index

        return helper(len(nums) - 1)

        
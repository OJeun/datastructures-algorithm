class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        longest = 1
        n = len(nums)
        dp = [1] * n

        for curr in range(1, n):
            temp_to_track_longest = 1
            for prev in range(curr):
                if nums[curr] > nums[prev]:
                    temp_to_track_longest = max(temp_to_track_longest, dp[prev] + 1)
            dp[curr] = temp_to_track_longest
            longest = max(longest,temp_to_track_longest)
        return longest


            

                
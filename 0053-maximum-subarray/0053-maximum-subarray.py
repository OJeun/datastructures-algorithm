class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]

        left = 0

        for right in range(1, len(nums)):
            currSum += nums[right]

            if currSum <= 0 or (currSum > 0 and currSum < nums[right]):
                left = right
                currSum = nums[left]

            maxSum = max(maxSum, currSum)

        return maxSum
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        multiply = [1]
        acc_multiply = 1

        for i in range(1, len(nums)):
            multiply.append(nums[i-1] * multiply[i-1])

        for j in range(len(nums) -2, -1, -1):
            acc_multiply *= nums[j + 1]
            multiply[j] *= acc_multiply

        return multiply

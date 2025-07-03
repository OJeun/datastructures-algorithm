class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        acc_xor = 0

        for num in nums:
            acc_xor = acc_xor ^ num

        return acc_xor
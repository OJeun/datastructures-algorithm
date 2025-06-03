class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            bit = n >> i & 1
            result = (result << 1) | bit

        return result

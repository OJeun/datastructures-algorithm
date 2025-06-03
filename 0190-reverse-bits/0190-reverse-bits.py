class Solution:
    def reverseBits(self, n: int) -> int:
        result = ""

        for i in range(31, -1, -1):
            bit = n >> i & 1
            result = str(bit) + result

        return self.binaryToInt(result)



    def binaryToInt(self, n:str) -> int:
        result = 0

        for bit in n:
            result = result * 2 + int(bit)

        return result



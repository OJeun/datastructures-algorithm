class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        divided_n = n

        while divided_n != 0:
            if divided_n % 2  == 1:
                result += 1
            divided_n = divided_n // 2

        return result
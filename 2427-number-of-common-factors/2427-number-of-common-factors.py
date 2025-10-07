class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        smaller = min(a, b)
        count = 0

        for factor in range(1, smaller + 1):
            if a % factor == 0 and b % factor == 0:
                count += 1

        return count
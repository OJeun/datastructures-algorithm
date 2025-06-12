class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        carry = 1

        while n > 0:
            digit = digits[n - 1]
            add_one = digit + carry

            if add_one >= 10:
                carry = 1
                digits[n-1] = add_one - 10
            else:
                digits[n-1] = add_one
                carry = 0
                break
            n -= 1

        if carry == 1:
            digits.insert(0, 1)

        return digits
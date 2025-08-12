class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1

        for index in range(len(digits)-1, -1, -1):
            digits[index] += carry
            digit = digits[index]
            
            digits[index] = digit % 10
            carry = digit // 10

        if carry != 0:
            digits.insert(0, carry)

        return digits

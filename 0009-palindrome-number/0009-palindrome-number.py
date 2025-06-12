class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0 or x < 10:
            return True
        if x % 10 == 0:
            return False

        number = x
        rest_half = 0

        while number > rest_half:
            digit = number % 10
            number //= 10

            rest_half = rest_half * 10 + digit

        if rest_half > number:
            return True if number == (rest_half // 10) else False
        else:
            return number == rest_half
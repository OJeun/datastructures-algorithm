import math
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        str_n = str(n)

        while True:
            square_sum = 0
            for digit in str_n:
                square_sum += pow(int(digit), 2)

            if square_sum == 1:
                return True
            
            if square_sum in seen:
                return False
            
            seen.add(square_sum)

            str_n = str(square_sum)


            
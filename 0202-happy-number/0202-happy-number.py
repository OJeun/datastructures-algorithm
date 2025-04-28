import math
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            new_n = 0
            digit = n % 10
            new_n += digit * digit
            n //= 10

            if new_n in seen:
                return False
            
            seen.add(new_n)

        return True

        

            
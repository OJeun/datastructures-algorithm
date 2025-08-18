class Solution:
    def isHappy(self, n: int) -> bool:
        
        digit_sum = n
        seen = set()
        seen.add(digit_sum)

        while digit_sum != 1:
            number = digit_sum
            digit_sum = 0

            while number != 0:    
                digit_sum += pow(number % 10, 2)
                number = number // 10
                
            if digit_sum in seen:
                return False
            seen.add(digit_sum)
        
        return True

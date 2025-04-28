import math
class Solution:
    def isHappy(self, n: int) -> bool:
        sum_of_squares = n
        squares_set = set()
        squares_set.add(n)

        while True:
            num_digits = int(math.log(sum_of_squares, 10))
            new_sum = 0
            while num_digits >= 0:
                pow_digits = pow(10, num_digits)
                digit = sum_of_squares // pow_digits
                new_sum += pow(digit, 2)
                
                sum_of_squares %= pow_digits
                num_digits -= 1

            sum_of_squares = new_sum 
            
            if sum_of_squares == 1:
                return True
            
            if sum_of_squares in squares_set:
                return False

            squares_set.add(new_sum)
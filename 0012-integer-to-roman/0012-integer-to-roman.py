import math


class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        roman_numerals = ""

        # 3749, exp = 3
        exp = int(math.log10(num))

        for e in range(exp, -1, -1):
            digit = pow(10, e)
            number = num // digit
            number_digit = number * digit
            
            if number_digit in symbols:
                roman_numerals += symbols[number_digit]
            else:
                if digit == 3 or number < 5:
                    roman_numerals += number * symbols[digit]
                else:
                    roman_numerals += symbols[5 * digit]
                    rest = number - 5
                    roman_numerals += rest * symbols[digit]
            
            num = num % digit

        return roman_numerals


            
            
                


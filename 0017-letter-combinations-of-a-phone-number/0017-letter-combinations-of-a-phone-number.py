class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def combinations(digits, combination):
            if len(digits) == 0:
                if combination:
                    result.append("".join(combination)) 
                return

            letters = digit_to_letters[digits[0]]

            for letter in letters:
                combination.append(letter)
                combinations(digits[1:], combination)
                combination.pop()
        
        combinations(digits, [])
        return result
                


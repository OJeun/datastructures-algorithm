class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        n = len(digits)
        res, sol = [], []

        if digits == "":
            return []

        def backtracking(index):
            if len(sol) == n:
                res.append("".join(sol))
                return

            for char in digit_to_letters[digits[index]]:
                sol.append(char)
                backtracking(index + 1)
                sol.pop()

        backtracking(0)
        return res

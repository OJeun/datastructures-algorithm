class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1

        while s[end] == " ":
            end -= 1

        last_char_in_substring = end 

        while end >= 0 and s[end] != " ":
            end -= 1

        return last_char_in_substring - end 
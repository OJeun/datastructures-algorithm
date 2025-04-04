class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_char_index = len(s) - 1
        length_of_last_word = 0

        while s[last_char_index] == " ":
            last_char_index -= 1

        while last_char_index > -1 and s[last_char_index] != " ":
            length_of_last_word += 1
            last_char_index -= 1

        return length_of_last_word
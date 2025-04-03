class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        first_word = strs[0]

        for i in range(len(first_word)):
            is_same = True
            char = first_word[i]

            for word in strs[1:]:
                if i > len(word) - 1:
                    is_same = False
                    break
                if i < len(word) and word[i] != char:
                    is_same = False
                    break

            if is_same:
                result += char
            else:
                break

        return result

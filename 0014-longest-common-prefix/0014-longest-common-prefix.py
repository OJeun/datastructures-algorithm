class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        is_prefix = True
        
        # pointer?
        pointer = 0

        while is_prefix and pointer < len(strs[0]):
            str_at_pointer = strs[0][pointer]

            for i in range(1, len(strs)):
                word = strs[i]
                if pointer >= len(word) or str_at_pointer != word[pointer]:
                    is_prefix = False
                    break

            if is_prefix:
                result += str_at_pointer

            pointer += 1

        return result

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_index = 0

        n_length = len(needle)
        h_length = len(haystack)

        while h_index <= h_length - n_length:
            for offset in range(n_length):
                if haystack[h_index + offset] != needle[offset]:
                    h_index += 1
                    break

                if offset == n_length - 1:
                    return h_index
        return -1
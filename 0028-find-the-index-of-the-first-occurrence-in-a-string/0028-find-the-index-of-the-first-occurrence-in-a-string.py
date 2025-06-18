class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_index = 0
        n_index = 0
        n_length = len(needle)
        h_length = len(haystack)

        if n_length > h_length:
            return -1

        while n_index < n_length and h_index < h_length:
            while needle[n_index] == haystack[h_index]:
                if n_index == n_length - 1:
                    return h_index - n_length + 1
                n_index += 1
                h_index += 1
            n_index = 0
            h_index += 1
             
        return -1
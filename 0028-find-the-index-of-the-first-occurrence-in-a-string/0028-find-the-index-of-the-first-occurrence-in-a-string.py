class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_index = 0
        h_start = 0
        n_index = 0
        n_length = len(needle)
        h_length = len(haystack)

        while h_index < h_length:
            if haystack[h_index] == needle[n_index]:
                h_start = h_index
                while h_index < h_length and n_index < n_length and haystack[h_index] == needle[n_index]:
                    if n_index == n_length - 1:
                        return h_start
                    h_index += 1
                    n_index += 1
            
            h_start += 1
            h_index = h_start
            n_index = 0

        return -1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_index = 0
        n_index = 0
        h_length = len(haystack)
        n_length = len(needle)

        while h_index <= h_length - n_length:
            for i in range(n_length):
                if haystack[h_index + i] != needle[i]:
                    h_index += 1
                    break
                
                if i == n_length - 1:
                    return h_index
        
        return -1
        


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        # create a variable to track the max substring length
        max_length = 1
        # define two pointers, start and end
        end = 1 
        start = 0
        seen = set(s[0])

        # Iterate string and adjust two pointer not to contain duplicates
        while start < len(s) and end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end += 1

            else: # s[end] is in seen
                seen.remove(s[start])
                start += 1

            max_length = max(end - start, max_length)

        return max_length


        # s = "abcbba"


        # Return the max substring length
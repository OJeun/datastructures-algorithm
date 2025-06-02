class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_length = len(s)
        distinct_char = set()
        max_length = 1
        left = 0

        if s_length == 0:
            return 0

        for right in range(s_length):
            char = s[right]

            if char not in distinct_char:
                distinct_char.add(char)
            else:
                max_length = max(max_length, right - left)
                while s[left] != char:
                    distinct_char.remove(s[left])
                    left += 1
                left += 1
        max_length = max(max_length, right - left + 1)
        return max_length

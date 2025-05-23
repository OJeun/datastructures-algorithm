class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length_s = len(s)
        set_char = set()

        longest = 0

        left = 0
        for right in range(length_s):
            right_char = s[right]
            if right_char in set_char:
                while right_char in set_char:
                    set_char.remove(s[left])
                    left += 1
                set_char.add(right_char)
            else:
                set_char.add(right_char)
                longest = max(longest, len(set_char))

        return longest

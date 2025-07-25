class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        start = 0
        seen = set()
        seen.add(s[start])

        for end in range(1, len(s)):
            current = s[end]
            while current in seen:
                seen.remove(s[start])
                start += 1

            seen.add(current)
            max_length = max(len(seen), max_length)

        return max_length
        
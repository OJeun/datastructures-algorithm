class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        frequency = dict()
        odd_freq_chars = 0

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        for char, freq in frequency.items():
            pair = freq // 2
            remainder = freq % 2

            if pair > 0:
                count += (pair * 2)

            if remainder == 1:
                odd_freq_chars += 1

        if odd_freq_chars:
            count += 1
            
        return count
    
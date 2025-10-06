class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        frequency = dict()
        is_single = False

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        for char, freq in frequency.items():
            pair = freq // 2
            if pair > 0:
                count += (pair * 2)

            if freq % 2 == 1 and not is_single:
                count += 1
                is_single = True 

        return count
    
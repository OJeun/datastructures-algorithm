class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # define a dictionary to store freqeucny of each char in s
        alphabets = [0] * 26

        if len(s) != len(t):
            return False

        for char in s:
            position = ord(char) - ord('a')
            alphabets[position] += 1

        # iterate t using for loop
        for char in t:
            position = ord(char) - ord('a')
            if alphabets[position] > 0:
                alphabets[position] -= 1
            else:
                return False
        
        # return True
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # define a dictionary to store freqeucny of each char in s
        frequencies = dict()

        if len(s) != len(t):
            return False

        for char in s:
            frequencies[char] = frequencies.get(char, 0) + 1

        # iterate t using for loop
        for char in t:
            # check each char is in dict
            if char in frequencies and frequencies[char] > 0:
                # if it does, decrease count by 1
                frequencies[char] -= 1
            # else: return False
            else:
                return False
        
        # return True
        return True
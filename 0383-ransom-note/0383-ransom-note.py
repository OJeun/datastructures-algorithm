class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary where the key is letter, value is count
        letters = dict()
        for char in magazine:
            letters[char] = letters.get(char, 0) + 1

        # iterate each character in ransomNote 
        for char in ransomNote:
            # check current character exists in dict, and its cound is at least 1
            count = letters.get(char)
            
            if not count or count < 1:
                return False
            else:
                letters[char] -= 1
                # if it is not, return False
                # if it is, decrease its count by 1 and continue
            
        # If I get through the entire for loop, return True
        return True
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        
        for i in range(len(magazine)):
            char = magazine[i]
            magazine_dict[char] = magazine_dict.get(char, 0) + 1

        for char in ransomNote:
            if magazine_dict.get(char) is not None:
                occurence = magazine_dict.get(char)
                if occurence > 0:
                    magazine_dict[char] = occurence - 1
                else:
                    return False
            else:
                return False

        return True

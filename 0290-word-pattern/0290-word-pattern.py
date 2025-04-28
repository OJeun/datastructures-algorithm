class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        pattern_set = set()
        s_list = s.split(" ")

        if len(pattern) != len(s_list):
            return False

        for i in range(len(pattern)):
            pattern_char = pattern[i]
            word = s_list[i]
            mapped_word = pattern_dict.get(pattern_char) 
            if mapped_word:
                if word != mapped_word:
                    return False
            else: 
                if word not in pattern_set:
                    pattern_dict[pattern_char] =  word
                    pattern_set.add(word)
                else:
                    return False
        return True

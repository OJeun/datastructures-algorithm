class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}

        if len(s) != len(t):
            return False

        for s_char in s:
            s_dict[s_char] = s_dict.get(s_char, 0) + 1
        
        for t_char in t:
            if t_char in s_dict and s_dict.get(t_char) > 0:
                s_dict[t_char] = s_dict[t_char] - 1
            else:
                return False
        
        return True
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomorphic_dict = {}
        isomorphic_set = set()

        for i in range(len(s)):
            mapped_char = isomorphic_dict.get(s[i])

            if mapped_char is None and t[i] not in isomorphic_set:
                isomorphic_dict[s[i]] = t[i]
                isomorphic_set.add(t[i])
            else:
                if mapped_char != t[i]:
                    return False
            
        return True
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        complete_word = []
        p_freq = dict()
        s_freq = dict()
        count = 0

        for char in p:
            p_freq[char] = p_freq.get(char, 0) + 1

        p_length = len(p_freq)

        l, r = 0, 0

        while r < len(s):
            char = s[r]
            if char in p_freq:
                s_freq[char] = s_freq.get(char, 0) + 1
                if s_freq[char] == p_freq[char]:
                    count += 1
            

            # if window size == length
            if r - l + 1 == len(p):
                # if count is == length
                if count == p_length:
                    # then increase complete_word += 1
                    complete_word.append(l)
        
                
                char_at_l = s[l]
                if char_at_l in s_freq:
                    if s_freq[char_at_l] == p_freq[char_at_l]:
                        count -= 1
                    s_freq[char_at_l] -= 1
                l += 1

            r += 1

        return complete_word
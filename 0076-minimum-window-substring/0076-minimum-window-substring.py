from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = dict()
        have = defaultdict(int)
        counts = 0
        output = ''
        left = 0

        for char in t:
            need[char] = need.get(char, 0) + 1

        for right in range(len(s)):
            curr_char = s[right]
            if curr_char in need:
                have[curr_char] += 1
                if have[curr_char] == need[curr_char]:
                    counts += 1

            if counts == len(need):
                while counts == len(need):
                    left_char = s[left]
                    if left_char in need:
                        have[left_char] -= 1
                        if have[left_char] < need[left_char]:
                            counts -= 1

                    left += 1
 

                if right - left + 2 >= len(t):
                    if not output:
                        output = s[left-1:right+1]
                    else:
                        if right - left + 2 < len(output):
                            output = s[left-1:right+1]

        return output
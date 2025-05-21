class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        s_length = len(s)
        word_dict_set = set(wordDict)
        memo = [None] * s_length  

        def helper(index):
            if index == s_length:
                return True
            if memo[index] is not None:
                return memo[index]

            for end in range(index + 1, s_length + 1):
                if s[index:end] in word_dict_set and helper(end):
                    memo[index] = True
                    return True

            memo[index] = False
            return False

        return helper(0)

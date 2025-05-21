class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        s_length = len(s)
        set_word_dict = set(wordDict)
        memoization = [None] * s_length

        def helper(index):
            if memoization[index] is not None:
                return memoization[index]
            
            for end in range(index + 1, s_length + 1):
                word = s[index : end]

                if word in set_word_dict:
                    if end == s_length:
                        memoization[index] = True
                        return True
                    if helper(end):
                        memoization[index] = True
                        return True
            
            memoization[index] = False
            return False

        return helper(0)

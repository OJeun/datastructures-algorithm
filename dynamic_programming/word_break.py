def word_break_recursive(s, word_dict):
    length_s = len(s)
    dp = []

    def helper(pointer):
        if pointer < 0:
            return True
        
        for word in word_dict:
            length_word = len(word)
            substring = s[pointer - length_word + 1: pointer+1]
            if substring in word_dict:
                return helper(pointer - length_word)
            
        return False
    return helper(length_s -1)

# Time Complexity = O(n^3)
# Space Complexity = O(n)
def word_break_recursive_2(s, word_dict):
    length_s = len(s)

    def helper(pointer):
        if pointer < 0:
            return True
        
        for word in word_dict:
            length_word = len(word)
            substring = s[pointer - length_word + 1: pointer+1] # O(n)
            if substring == word and helper(pointer - length_word):
                return True
        return False
    return helper(length_s -1)
    
print(word_break_recursive_2("bbbbbabbbbb", ["b", "bb", "bbb"]))


# Time Complexity = O(n * m * k) m = length of dict, k = average word length in dictionary
def word_break_memoization(s, word_dict):
    length_s = len(s)
    dp = [-1] * length_s

    def helper(pointer):
        if pointer < 0:
            return True
        
        if dp[pointer] != -1:
            return True
        
        for word in word_dict:
            length_word = len(word)
            substring = s[pointer - length_word + 1: pointer+1]
            if substring == word and helper(pointer - length_word):
                dp[pointer] = True
                return dp[pointer]
            
        dp[pointer] = False
        return dp[pointer]
    
    return helper(length_s -1)
        
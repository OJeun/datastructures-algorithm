class Solution:
    def groupAnagrams(self, strs):
        anagrams_dict = {}
        index = 0
        anagrams = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            sorted_word_index = anagrams_dict.get(sorted_word)
            if anagrams_dict.get(sorted_word) is None:
                anagrams_dict[sorted_word] = index
                anagrams.append([word])
                index += 1
            else:
                anagrams[sorted_word_index].append(word)
        
        return anagrams



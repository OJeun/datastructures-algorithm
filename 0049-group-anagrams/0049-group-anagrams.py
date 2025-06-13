class Solution:
    def groupAnagrams(self, strs):
        output = []
        index = 0

        anagram_dict = dict()

        for word in strs:
            sorted_word = "".join(sorted(word))
            is_anagram = anagram_dict.get(sorted_word)

            if is_anagram is not None:
                index_in_output = is_anagram
                output[index_in_output].append(word)
            else:
                anagram_dict[sorted_word] = index
                output.append([word])
                index += 1
            
            

        return output
            
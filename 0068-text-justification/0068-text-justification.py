class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        words_index = 0
        n = len(words)
        res = []
        
        while words_index < n:
            char_count = len(words[words_index])
            last = words_index + 1

            while last < n and char_count + 1 + len(words[last]) <= maxWidth:
                char_count += 1 + len(words[last])
                last += 1

            words_in_line = last - words_index
            total_white_spaces = maxWidth - sum(len(words[i]) for i in range(words_index, last))
            
   

            line = ""
            if last == n or words_in_line == 1:
                line += " ".join(words[words_index:last])
                line += " " * (maxWidth - len(line))
            else:
                nums_of_white_spaces = total_white_spaces // (words_in_line - 1)
                extra_spaces = total_white_spaces % (words_in_line - 1)

                for i in range(words_index, last - 1):
                    line += words[i]
                    line += " " * (nums_of_white_spaces + (1 if i - words_index < extra_spaces else 0))
                line += words[last - 1]

            words_index = last

            res.append(line)

        return res
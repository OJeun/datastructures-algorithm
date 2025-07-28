class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_index = [-1] * 26 # index = char position in alphabets (a = 0, b= 1) # value = last index of that character in s
        output = []

        partition_end = 0
        partition_start = -1

        for index, char in enumerate(s):
            position = ord(char) - ord('a')
            char_index[position] = index

        for index, char in enumerate(s): 
            position = ord(char) - ord('a')
            last_index = char_index[position]

            if index <= last_index:
                partition_end = max(partition_end, last_index)

            if index == partition_end:
                partition_length = partition_end - partition_start
                output.append(partition_length)
                partition_start = index

        return output

                